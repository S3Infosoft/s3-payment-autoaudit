from django.urls import re_path, path
from . import views

urlpatterns = [
    re_path(r"^(?P<company>[\w]+)/"
            r"(?P<day1>[0-9]{2})-(?P<month1>[0-9]{2})-(?P<year1>[0-9]{4})/"
            r"(?P<day2>[0-9]{2})-(?P<month2>[0-9]{2})-(?P<year2>[0-9]{4})/$",
            views.Type1ListAPIView.as_view(), name="list_api"),
    path('icici/', views.Type8ListAPIView.as_view(), name="list_api"),
    path('mswipe/', views.Type9ListAPIView.as_view(), name="list_api"),
]
