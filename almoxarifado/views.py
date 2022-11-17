from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages

def index(request):
    materiais=Material.objects.all()
    context={
        'materiais': materiais
    }
    return render(request, 'almoxarifado/index.html', context)

def listar_tipo_materiais(request):
    context={
        'tipos':Tipo_Material.objects.all()
    }
    return render(request, 'almoxarifado/listar_materiais.html', context)

def adicionar_tipo_materiais(request):
    if request.method=='POST':
        form=Tipo_Material_Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tipo de material cadastrado!')
            return redirect('alm_listar_tipos')
    else:
        form=Tipo_Material_Form()

    context={
        'form': form
    }
    return render(request, 'almoxarifado/adicionar_tipo_materiais.html', context)

def adicionar_material(request):    
    if request.method=='POST':
        form=Material_Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Material cadastrado!')
            return redirect('alm_listar_tipos')
    else:
        form=Material_Form()

    context={
        'form': form
    }
    return render(request, 'almoxarifado/adicionar_novo_material.html', context)


def adicionar_material_ao_estoque(request):    
    if request.method=='POST':
        form=Log_estoque_Form(request.POST)
        form_tipo=Exibir_Tipo_Material_Form(request.POST)
        if form.is_valid():
            log=form.save()            
            material=Material.objects.get(id=log.material.id)            
            log.qnt_em_estoque=material.qnt_em_estoque            
            material.qnt_em_estoque=material.qnt_em_estoque+log.add_quantidade
            material.save()
            log.save()
            if log.add_quantidade == 1:
                messages.success(request, f"{log.add_quantidade} nova unidade adicionada ao estoque. Total: {material.qnt_em_estoque}.")
            else: 
                messages.success(request, f"{log.add_quantidade} novas unidades adicionadas ao estoque. Total: {material.qnt_em_estoque}.")
            return redirect('alm_index')
    else:
        form=Log_estoque_Form()
        form_tipo=Exibir_Tipo_Material_Form()

    context={
        
        'form': form,
        'form_tipo': form_tipo
    }
    return render(request, 'almoxarifado/adicionar_material_ao_estoque.html', context)
