from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_topic, name='index'),
]
