from django.urls import path
from .views import register_view, login_view, logout_view, dashboard_view, add_transaction_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('add_transaction/', add_transaction_view, name='add_transaction'),
]
