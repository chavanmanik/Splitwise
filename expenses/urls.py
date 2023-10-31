# expenses/urls.py
from django.urls import path
from . views import home
from . import views

urlpatterns = [
    path('',home,name='homepage'),
    path('create_expense/', views.create_expense, name='create_expense'),
    path('get_balances/<str:user_id>/', views.get_balances, name='get_balances'),
]
