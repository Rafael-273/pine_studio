from django.views.generic import ListView, DetailView
from ..models import Pack


class PackListView(ListView):
    model = Pack
    template_name = 'front/packs.html'
    context_object_name = 'packs'
    paginate_by = 9

    def get_queryset(self):
        return Pack.objects.all().order_by('name')
    

class PackDetailView(DetailView):
    model = Pack
    template_name = 'front/pack_detail.html'
    context_object_name = 'pack'