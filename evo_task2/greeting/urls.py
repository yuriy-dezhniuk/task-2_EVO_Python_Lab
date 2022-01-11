from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='greeting'),
    path('names', views.name_list, name='names')
]