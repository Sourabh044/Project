from django.urls import path
from . import views
from . import templates 
urlpatterns = [
    path('', views.Hotel),
    path('hotel', views.Hotel),
    path('Signup', views.Signup),
]