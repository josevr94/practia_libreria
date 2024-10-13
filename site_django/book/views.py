from django.shortcuts import render
import datetime

# Create your views here.

def menu(request):
    return render(request,'book/menu.html')

def index(request):
    return render(request,'book/index.html')
    
    
def book(request):
    return render(request,'book/books.html')

def obtener_fecha(request):
    fecha_actual = datetime.datetime.now()
    return render(request,'book/fecha.html',{'fecha':fecha_actual})

def palindromo(request,name):
    return render(request,'book/palindro.html',{'name': name})

def titulos(request):
    libros = [
    {'titulo': 'Cien años de soledad', 'autor': 'Gabriel García Márquez', 'valoracion': 500},
    {'titulo': '1984', 'autor': 'George Orwell', 'valoracion': 470},
    {'titulo': 'Orgullo y prejuicio', 'autor': 'Jane Austen', 'valoracion': 460},
    {'titulo': 'El gran Gatsby', 'autor': 'F. Scott Fitzgerald', 'valoracion': 450},
    {'titulo': 'Matar a un ruiseñor', 'autor': 'Harper Lee', 'valoracion': 480},
    {'titulo': 'Los miserables', 'autor': 'Victor Hugo', 'valoracion': 470},
    {'titulo': 'Crimen y castigo', 'autor': 'Fiódor Dostoyevski', 'valoracion': 460},
    {'titulo': 'Don Quijote de la Mancha', 'autor': 'Miguel de Cervantes', 'valoracion': 490},
    {'titulo': 'El señor de los anillos', 'autor': 'J.R.R. Tolkien', 'valoracion': 490},
    {'titulo': 'El alquimista', 'autor': 'Paulo Coelho', 'valoracion': 450},
    {'titulo': 'El amor en los tiempos del cólera', 'autor': 'Gabriel García Márquez', 'valoracion': 490},
    {'titulo': 'Rayuela', 'autor': 'Julio Cortázar', 'valoracion': 480},
    {'titulo': 'La sombra del viento', 'autor': 'Carlos Ruiz Zafón', 'valoracion': 470},
    {'titulo': 'El nombre de la rosa', 'autor': 'Umberto Eco', 'valoracion': 460},
    {'titulo': 'La metamorfosis', 'autor': 'Franz Kafka', 'valoracion': 455},
    {'titulo': 'Cumbres borrascosas', 'autor': 'Emily Brontë', 'valoracion': 450},
    {'titulo': 'Ulises', 'autor': 'James Joyce', 'valoracion': 445},
    {'titulo': 'Fahrenheit 451', 'autor': 'Ray Bradbury', 'valoracion': 440},
    {'titulo': 'El guardián entre el centeno', 'autor': 'J.D. Salinger', 'valoracion': 435},
    {'titulo': 'La isla del tesoro', 'autor': 'Robert Louis Stevenson', 'valoracion': 430}
]
    return render(request,'book/lista.html',{'libros':libros})