from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('upload.urls')),
    path("api/v1/audit/", include("upload.api.urls")),
]
