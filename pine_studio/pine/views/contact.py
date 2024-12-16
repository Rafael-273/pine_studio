from django.views.generic import TemplateView, ListView
from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib import messages
from ..forms.contact import ContactForm
from ..views.email_management import EmailManagementView


class ContactView(TemplateView):
    template_name = 'front/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_email'] = 'contatoondecomeremmarica@gmail.com'
        context['form'] = ContactForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)

        if form.is_valid():
            contact_message = form.save()

            subject = f"Nova mensagem de {contact_message.name} - {contact_message.subject}"
            context = {
                'name': contact_message.name,
                'email': contact_message.email,
                'number': contact_message.phone,
                'subject': contact_message.subject,
                'message': contact_message.message
            }

            template_name = 'email/contact_email.html'
            to_emails = ['contatoondecomeremmarica@gmail.com', 'ondecomeremmarica@gmail.com']
            email_sent = EmailManagementView.send_email(subject, template_name, context, to_emails)

            if email_sent:
                messages.success(request, 'Mensagem enviada com sucesso!')
                return redirect('contact')

            else:
                messages.error(request, 'Falha ao enviar o e-mail.')
                return redirect('contact')

        return JsonResponse({'status': 'error', 'message': 'Dados inválidos.'}, status=400)