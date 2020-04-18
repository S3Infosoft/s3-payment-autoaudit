from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('fileupload/', views.fileupload, name='fileupload'),
    path('manualaudit/', views.manualaudit, name='manualaudit'),
    path('icici/', views.icici_view, name='icici'),
    path('mswipe/', views.mswipe_view, name='mswipe'),
    path('masterdata/', views.send_master_data, name='send_master_data'),

]
