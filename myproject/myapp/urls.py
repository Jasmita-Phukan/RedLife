from django.urls import path
from . import views

urlpatterns = [

    path('', views.about, name='about'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('blooddir/', views.blooddir, name='blooddir'),
    path('contact/', views.contact, name='contact'),
    path('donateblood/', views.donateblood, name='donateblood'),
    path('submit_details/', views.submit_details, name='submit_details'),
    path('details2/', views.details2, name='details2'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('confirmation2/', views.confirmation2, name='confirmation2'),
]
