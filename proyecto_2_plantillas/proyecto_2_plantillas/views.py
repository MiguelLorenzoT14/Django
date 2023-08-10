from django.shortcuts import render

def simple(request):
    return render(request,'simple.html',{})

def dinamico(request,name):
    categoria = ['code','design','marketing']
    contexto = {'name':name,'categoria':categoria}
    return render(request,'dinamico.html',contexto)