from . import views
from django.urls import path

urlpatterns = [
    path('', views.SpaceList.as_view(), name='home')
]