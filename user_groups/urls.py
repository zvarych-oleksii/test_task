from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index_page, name="home"),
    path('users/create/', views.CustomUserCreateView.as_view(), name='register'),
    path('groups/create/', views.CustomGroupCreateView.as_view(), name='create_group'),
    path('users/', views.CustomUserListView.as_view(), name='user_list'),
    path('groups/', views.CustomGroupListView.as_view(), name='group_list'),
    path('user/<int:pk>/edit/', views.CustomUserUpdateView.as_view(), name='edit_user'),
    path('user/<int:pk>/delete/', views.CustomUserDeleteView.as_view(), name='delete_user'),
    path('group/<int:pk>/edit/', views.CustomGroupUpdateView.as_view(), name='edit_group'),
    path('group/<int:pk>/delete/', views.CustomGroupDeleteView.as_view(), name='delete_group'),
]
