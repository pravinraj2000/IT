from django.urls import path
from .import views

urlpatterns = [
    path('App/',views.index, name='App-index'),
    path('post_detail/<int:pk>/', views.post_detail, name='App-post_detail'),
    path('post_edit/<int:pk>/', views.post_edit, name='App-post_edit'),
    path('post_delete/<int:pk>/', views.post_delete, name='App-post_delete'),
]