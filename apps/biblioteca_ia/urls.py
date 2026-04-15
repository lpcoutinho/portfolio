from django.urls import path
from . import views

app_name = 'biblioteca_ia'

urlpatterns = [
    path('', views.biblioteca_home, name='home'),
    path('categoria/<slug:slug>/', views.categoria_detalhe, name='categoria'),
    path('categoria/<slug:slug>/prompt/<int:pk>/', views.prompt_detalhe, name='prompt'),
]
