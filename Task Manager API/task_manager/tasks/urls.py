from django.urls import path
from .views import TaskListCreateView, TaskDetailView, CustomTokenObtainPairView, CustomTokenRefreshView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('auth/token/', TokenObtainPairView.as_view(), name = 'token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name = 'token_refresh'),
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('taks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
]
