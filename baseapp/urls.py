from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.dodaj, name='dodaj'),
    path('delete/<id>', views.usun, name='usun'),
    path('edit/<id>', views.edytuj, name='edytuj'),
    path('switch/<id>', views.switchDone, name='switch'),
]
