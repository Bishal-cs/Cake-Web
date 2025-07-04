from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('home/', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('about/', views.about, name='about'),
    path('order/', views.order, name='order'),
    path('contact/', views.contact, name='contact'),
]