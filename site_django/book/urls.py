from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('book/',views.book, name='book'),
    path('fecha/',views.obtener_fecha, name='fecha'),
    
]