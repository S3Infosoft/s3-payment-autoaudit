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
    path('customercreate/', views.CustomerCreateView.as_view(), name='customer_create'),
    path('customerlist/', views.CustomerListView.as_view(), name='customer_list'),
    path('customerdetail/<int:pk>/', views.CustomerDetailView.as_view(), name='customer_detail'),
    path("customerupdate/<int:pk>/", views.update_customer, name="customer_update"),
    path("customerdelete/<int:pk>/", views.CustomerDeleteView.as_view(), name="customer_delete"),
    path('checkincreate/', views.CustomerCheckInCreateView.as_view(), name='checkin_create'),
    path('checkinlist/', views.CustomerCheckInListView.as_view(), name='checkin_list'),
    path('checkindetail/<int:pk>', views.CustomerCheckInDetailView.as_view(), name='checkin_detail'),
    path("checkinupdate/<int:pk>/", views.update_customercheckin, name="checkin_update"),
    path("checkindelete/<int:pk>/", views.CustomerCheckInDeleteView.as_view(), name="checkin_delete"),
    path('cashentrycreate/', views.CashEntryCreateView.as_view(), name='cashentry_create'),
    path('cashentrylist/', views.CashEntryListView.as_view(), name='cashentry_list'),
    path('cashentrydetail/<int:pk>', views.CashEntryDetailView.as_view(), name='cashentry_detail'),
    path("cashentryupdate/<int:pk>/", views.update_cashentry, name="cashentry_update"),
    path("cashentrydelete/<int:pk>/", views.CashEntryDeleteView.as_view(), name="cashentry_delete"),

]
