from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('custom-input/', views.custom_input, name='custom_input'),
    path('real-time-tracking/', views.real_time_tracking, name='real_time_tracking'),
    path('shap/', views.shap_explanation, name='shap_explanation'),
    path('result/', views.result,name="result")

]

