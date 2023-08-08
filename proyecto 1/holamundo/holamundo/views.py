from django.http import HttpResponse


def saludo(request):
   return HttpResponse("hola Mundo")

def despedida(request):
   return HttpResponse("hasta luego")