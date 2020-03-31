from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('fileupload/', views.fileupload, name='fileupload'),
    path('manualaudit/', views.manualaudit, name='manualaudit'),
]
