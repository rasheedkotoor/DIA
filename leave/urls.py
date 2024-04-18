from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('list/', views.leave_list, name='leave_list'),
    path('list/<int:leave_type>/', views.leave_list, name='leave_list'),
    path('add/', views.leave_add, name='leave_add'),
    path('<int:pk>/edit/', views.leave_edit, name='leave_edit'),
    path('<int:pk>/delete/', views.leave_delete, name='leave_delete'),
]