from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FormA, FormB
from .models import ModelA, ModelB
# Create your views here.

def index(request):
    if request.method == 'POST':
        form_a = FormA(request.POST, prefix='form_a')
        form_b = FormB(request.POST, prefix='form_b')
        
        if 'submit_form_a' in request.POST:
            if form_a.is_valid():
                form_a.save()
                messages.success(request, 'Form A submitted successfully')
                return redirect('success')
            
        if 'submit_form_b' in request.POST:
            if form_b.is_valid():
                form_b.save()
                messages.success(request, 'Form A submitted successfully!')
                return redirect('success')
    else:
        form_a = FormA(prefix= 'form_a')
        form_b = FormB(prefix= 'form_b')
    
    context ={
        'form_a':form_a , 
        'form_b':form_b
        }
    
    return render(request, 'index.html', context)



def success(request):
    model_a_data = ModelA.objects.all()  # Fetch all data from ModelA
    model_b_data = ModelB.objects.all()  # Fetch all data from ModelB

    context = {
        'model_a_data': model_a_data,
        'model_b_data': model_b_data,
    }
    return render(request, 'success.html', context)
