from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('students/', views.student_list_view, name='student_list'),
    path('students/add/', views.student_create_view, name='student_add'),
    path('students/<int:pk>/', views.student_detail_view, name='student_detail'),
    path('students/<int:pk>/edit/', views.student_update_view, name='student_edit'),
    path('students/<int:pk>/delete/', views.student_delete_view, name='student_delete'),
]
