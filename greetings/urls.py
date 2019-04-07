from django.urls import path
from . import views

app_name = 'greetings' # allows using 'greetings:index' for url and reverse_lazy methods
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('new', views.CreateView.as_view(), name='create'),
]
