from django.shortcuts import render
from .models import Cliente

def home(request):
    return render(request,'clientes/home.html')

def clientes(request):
    # Salvar os dados da tela para o banco de dados
    novo_cliente = Cliente()
    novo_cliente.nome = request.POST.get('nome')
    novo_cliente.email = request.POST.get('email')
    novo_cliente.razao = request.POST.get('razao')
    novo_cliente.cnpj = request.POST.get('cnpj')
    novo_cliente.endereco = request.POST.get('endereco')
    novo_cliente.celular = request.POST.get('celular')
    novo_cliente.save()
    
    # Exibir todos os clientes já cadastrados em uma nova página
    clientes = {
        'clientes': Cliente.objects.all()
    }

    # Retornar os dados para a página de listagem de clientes
    return render(request, 'clientes/clientes.html', clientes)