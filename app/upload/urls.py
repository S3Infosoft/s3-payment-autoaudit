from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('fileupload/', views.fileupload, name='fileupload'),
    path('manualaudit/', views.manualaudit, name='manualaudit'),
    path('icici/', views.icici_view, name='icici'),
    path('mswipe/', views.mswipe_view, name='mswipe'),
    re_path(r"^masterdata/(?P<month>[0-9]{2})/(?P<year>[0-9]{4})/",
            views.send_master_data, name="send_master_data"),
]
