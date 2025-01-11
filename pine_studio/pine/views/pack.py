from django.contrib import messages
from django.http import JsonResponse
from .email_management import EmailManagementView
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.db.models import Q
from ..models import Pack
from ..forms.contact import DownloadEmailForm


class PackListView(ListView):
    model = Pack
    template_name = 'front/packs.html'
    context_object_name = 'packs'
    paginate_by = 9

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        queryset = Pack.objects.all().order_by('-update_at')

        is_free = self.request.GET.get('is_free')
        if is_free == "true":
            queryset = queryset.filter(is_free=True)
        elif is_free == "false":
            queryset = queryset.filter(is_free=False)

        if query:
            queryset = queryset.filter(Q(name__icontains=query) | Q(description__icontains=query))

        return queryset


class PackDetailView(DetailView):
    model = Pack
    template_name = 'front/pack_detail.html'
    context_object_name = 'pack'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pack = self.object

        context['creatives_1080x1080'] = pack.creatives.filter(dimensions="1080x1080").exclude(carousels__isnull=False).order_by('created_at')
        context['creatives_1080x1350'] = pack.creatives.filter(dimensions="1080x1350").exclude(carousels__isnull=False).order_by('created_at')
        context['creatives_1080x1920'] = pack.creatives.filter(dimensions="1080X1920").exclude(carousels__isnull=False).order_by('created_at')
        
        creatives_with_carousels_square = {}
        creatives_with_carousels_vertical = {}

        creatives = pack.creatives.filter(carousels__isnull=False)
        for creative in creatives:
            carousels = list(creative.carousels.all())
            
            if creative.dimensions == '1080x1080':
                creatives_with_carousels_square[creative] = carousels
            elif creative.dimensions == '1080x1350':
                creatives_with_carousels_vertical[creative] = carousels

        context['creatives_carousels_square'] = creatives_with_carousels_square
        context['creatives_carousels_vertical'] = creatives_with_carousels_vertical
        
        context['form'] = DownloadEmailForm(pack=self.object)
        
        return context

    def post(self, request, *args, **kwargs):
        form = DownloadEmailForm(request.POST)
        pack = self.get_object()

        if form.is_valid():
            download_email = form.cleaned_data

            subject = f"Pack {download_email['pack'].name}"
            context = {
                'name': download_email['name'],
                'pack_name': download_email['pack'].name if download_email['pack'] else 'Pacote não especificado',
                'pack_link': download_email['pack'].sales_link
            }

            template_name = 'email/free_pack_email.html'
            to_emails = [download_email['email']]
            email_sent = EmailManagementView.send_email(subject, template_name, context, to_emails)

            if email_sent:
                form.save()
                messages.success(request, 'O pack foi enviado com sucesso para o seu e-mail! Verifique sua caixa de entrada e, se necessário, a pasta de spam')
                return redirect('pack_detail', slug=pack.slug)
            else:
                messages.error(request, 'Falha ao enviar o e-mail. Por favor, entre em contato conosco')
                return redirect('pack_detail', slug=pack.slug)

        return JsonResponse({'status': 'error', 'message': 'Dados inválidos.'}, status=400)