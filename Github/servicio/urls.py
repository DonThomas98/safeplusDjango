from django.urls import path

from . import views
from .views import Home
urlpatterns = [
    path('', views.Home, name='home'),
]
