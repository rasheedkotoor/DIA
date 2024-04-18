from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('student_list/', views.student_list, name='student_list'),
    path('student_add/', views.student_add, name='student_add'),
    path('<int:pk>/student_edit/', views.student_edit, name='student_edit'),
    path('<int:pk>/student_delete/', views.student_delete, name='student_delete'),
]