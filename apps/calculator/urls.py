from django.urls import path
from . import views

app_name = 'calculator'

urlpatterns = [
    path('', views.calculator_view, name='index'),
    path('calculate/', views.CalculateAjaxView.as_view(), name='calculate_ajax'),
]