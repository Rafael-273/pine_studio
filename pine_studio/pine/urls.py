from django.urls import path
from .views.home import HomeView
from .views.pack import PackListView, PackDetailView
from .views.about import AboutPageView
from .views.contact import ContactView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('packs/', PackListView.as_view(), name='packs'),
    path('quem_sou_eu/', AboutPageView.as_view(), name='about'),
    path('contato/', ContactView.as_view(), name='contact'),
    path('<slug:slug>/', PackDetailView.as_view(), name='pack_detail'),
]