from django.shortcuts import render
from .models import Cliente
from .forms import ClienteForm

# Create your views here.
def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request,'clientes/lista_clientes.html',{'clientes':clientes})


def inserir_cliente(request):
    print("oi")
    if request.method == "POST":
        form = ClienteForm(request.POST)
        print("oi1")
        if form.is_valid():
            print("oi2")
            form.save()
    else:
        print("oi3")
        form = ClienteForm()
    return render(request,'clientes/form_cliente.html',{'form':form})
