from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_book, name='register_book'),
]
