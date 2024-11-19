from django.urls import path
from .views import register_farmer, register_buyer, admin_dashboard, farmer_dashboard, buyer_dashboard

urlpatterns = [
    path('register/farmer/', register_farmer, name='register_farmer'),
    path('register/buyer/', register_buyer, name='register_buyer'),
]

from .views import user_login

urlpatterns += [
    path('login/', user_login, name='login'),
]


urlpatterns += [
    path('admin/dashboard/', admin_dashboard, name='admin_dashboard'),
    path('farmer/dashboard/', farmer_dashboard, name='farmer_dashboard'),
    path('buyer/dashboard/', buyer_dashboard, name='buyer_dashboard'),
]
