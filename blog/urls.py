from django.urls import path
from . import views

urlpatterns = [
    path('create_articles/', views.create_articles, name='create_articles')
]