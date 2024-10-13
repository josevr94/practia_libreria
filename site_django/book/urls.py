from django.urls import path
from . import views

urlpatterns = [
    path('',views.menu, name='menu'),
    path('index/',views.index, name='index'),
    path('book/',views.book, name='book'),
    path('fecha/',views.obtener_fecha, name='fecha'),
    path('palindro/<name>',views.palindromo, name='palindro'),
    
    
]