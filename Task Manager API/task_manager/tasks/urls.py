from django.urls import path
from .views import TaskListCreateView, TaskDetailView, CustomTokenObtainPairView, CustomTokenRefreshView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    ]
