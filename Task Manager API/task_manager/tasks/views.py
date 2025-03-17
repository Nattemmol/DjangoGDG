from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .models import Task
from .serializers import TaskSerializer, UserSerializer, CustomTokenObtainPairSerializer
from rest_framework.response import Response
# Create your views here.

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user or request.user.is_staff

class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Task.objects.all()
        return Task.objects.filter(owner=user)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Task.objects.all()
        return Task.objects.filter(owner=user)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    

class CustomTokenRefreshView(TokenRefreshView):
    pass