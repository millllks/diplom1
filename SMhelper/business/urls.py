from django.urls import path
from . import views

urlpatterns = [
    path('', views.page, name='main'),
    path('about', views.pageserv, name='services'),
    path('faqqv', views.pagefaq, name='faq'),
    path('bas', views.basic, name='basic')
]