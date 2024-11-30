from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/customer/', views.register_customer, name='register_customer'),
    path('login/customer/', views.customer_login, name='customer_login'),
    path('register/staff/', views.register_staff, name='register_staff'),
    path('login/staff/', views.staff_login, name='staff_login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/customer/', views.customer_dashboard, name='customer_dashboard'),
    path('submit-request/', views.submit_request, name='submit_request'),
    path('track-request/', views.track_request, name='track_request'),
    path('dashboard/staff/', views.staff_dashboard, name='staff_dashboard'),
    path('update-status/<int:service_id>/', views.update_status, name='update_status'),
]

