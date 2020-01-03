from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name=''),
    path('upload_file/', views.upload_file, name="upload_file"),

]