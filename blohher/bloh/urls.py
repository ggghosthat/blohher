from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='bloh-home'),
    path('about/', views.about, name='bloh-about')
]
