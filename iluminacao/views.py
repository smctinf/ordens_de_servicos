from django.shortcuts import render, redirect
from .forms import *

def index(request):
    return render(request, 'index.html')

def os_index(request):
    oss=OrdemDeServico.objects.all()
    context={
        'oss': oss
    }
    return render(request, 'iluminacao/index.html', context)


def add_os(request):
    if request.method=='POST':
        form=OS_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_os')
    else:
        form=OS_Form(initial={'tipo': '1'})
    context={
        'form': form
    }
    return render(request, 'iluminacao/adicionar_os.html', context)


def detalhes_os(request, id):
    os=OrdemDeServico.objects.get(id=id)
    if request.method=='POST':        
        pass
    else:
        pass
    context={
        'os': os
    }
    return render(request, 'iluminacao/detalhes_os.html', context)
