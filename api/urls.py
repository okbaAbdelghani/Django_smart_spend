from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('add/', views.addItem),
    path('users/add/', views.addUser),
    path('users/list/', views.getUsers),
    path('add_account/<int:user_id>/', views.addAccount, name='add-account'),
    path('get_accounts/<int:user_id>/', views.getAccounts, name='get-accounts'),
]

