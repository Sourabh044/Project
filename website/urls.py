from django.contrib import admin
from django.urls import path
from django.urls import include, path

from Hotel.views import Hotel
from website.settings import TEMPLATES
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Hotel.urls')),
    # path('Signup', include('Hotel.urls')),
]
