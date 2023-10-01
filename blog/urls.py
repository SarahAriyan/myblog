from . import views
from django.urls import path,include

urlpatterns = [
    path('create100/',views.create100),
]
