from django.urls import path
from . import views
urlpatterns = [
    path('', views.dashboard),
    # path('login/', views.login),
    # path('register/', views.register),
]
