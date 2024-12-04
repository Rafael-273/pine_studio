from django.views.generic import ListView, DetailView
from ..models import Pack


class PackListView(ListView):
    model = Pack
    template_name = 'front/pack.html'
    context_object_name = 'packs'
    paginate_by = 9

    def get_queryset(self):
        return Pack.objects.all().order_by('name')