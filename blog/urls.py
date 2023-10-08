from . import views
from django.urls import path,include

urlpatterns = [
    path('create100/',views.create100), 
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),

]
