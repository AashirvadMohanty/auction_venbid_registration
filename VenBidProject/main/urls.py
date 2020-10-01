from . import views
from django.urls import path

app_name = 'main'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
]