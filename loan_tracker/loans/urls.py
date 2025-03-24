from django.urls import path
from . import views

urlpatterns = [
    path('', views.loan_list, name='home'),
    path('loan_list/', views.home, name='loan_list'),
    path("loan/new/", views.loan_form, name="loan_new"),
    path('loan/edit/<int:id>/', views.loan_form, name='loan_edit'),
    path('loan/delete/<int:id>/', views.loan_delete, name='loan_delete'),
]