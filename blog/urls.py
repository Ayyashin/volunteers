from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post_list2/', views.post_list2, name='post_list2'),
    path('dos/', views.dos, name='dos'),
    path('service/', views.service, name='service'),
    path('partners/', views.partners, name='partners'),
    path('projects/', views.projects, name='projects'),
    path('otch/', views.otch, name='otch'),
    path('contacts/', views.contacts, name='contacts'),
    path('register/', views.register, name='register'),
    path('specialo/', views.specialo, name='specialo'),
    path('library/', views.library, name='library'),
    path('history/', views.history, name='history'),
    path('login/', views.login, name='login'),
]