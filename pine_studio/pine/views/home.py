from django.views.generic import ListView
from ..models import Creative


class HomeView(ListView):
    template_name = 'front/home.html'
    context_object_name = 'creatives'

    def get_queryset(self):
        return Creative.objects.filter(is_free=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)   
        context['featured_free_creatives'] = Creative.objects.filter(is_free=True, is_featured=True)
        return context
