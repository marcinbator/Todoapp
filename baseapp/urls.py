from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('dodaj/', views.dodaj, name='dodaj'),
    path('delete/<id>', views.usun, name='usun')
]
