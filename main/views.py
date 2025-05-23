from django.shortcuts import render

# Create your views here.
def home(request):
    print("Renderizando home.html")
    return render(request, 'home.html')