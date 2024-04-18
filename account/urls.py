from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('list/', views.account_list, name='account_list'),
    path('list/<int:account_type>/', views.account_list, name='account_list'),
    # path('accounts/', views.accounts_ajax, name='accounts_ajax'),
    path('add/', views.account_add, name='account_add'),
    path('<int:pk>/edit/', views.account_edit, name='account_edit'),
    path('<int:pk>/delete/', views.account_delete, name='account_delete'),
]