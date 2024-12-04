from django.urls import path
from .views.home import HomeView
from .views.pack import PackListView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('packs/', PackListView.as_view(), name='packs'),
]