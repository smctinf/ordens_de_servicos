from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

# def os_index(request):
#     return render(request, 'index.html')

@login_required
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
