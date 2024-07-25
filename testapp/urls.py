
from django.urls import path, include
from testapp import views

urlpatterns = [
    path('', views.home, name="home"),
    path('Cultural/', views.culturalPage, name="cultural"),
    path('Technical/', views.technicalPage, name="Technical"),
    path('Sport/', views.sportPage, name="sport"),
    path('Eco/', views.culturalPage, name="eco"),
    path('join/', views.joinPage, name="join")
]
