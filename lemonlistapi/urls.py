from django.urls import path
from . import views


urlpatterns = [
    path('lemonlist/', views.lemonslist)
]