from django.shortcuts import render,redirect
from .models import Receipe
# Create your views here.

def receipes(request):

    if request.method == 'POST':
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')

        Receipe.objects.create(
            receipe_name = receipe_name,
            receipe_description = receipe_description,
            receipe_image = receipe_image
        )

        return redirect('/')
    
    all_receipes = Receipe.objects.all()
    context = {'all_receipes':all_receipes}
    return render(request,'receipes.html',context)

def delete_receipe(request,id):
    queryset = Receipe.objects.get(id = id)
    queryset.delete()
    
    return redirect('/receipes/')

def update_receipe(request,id):
    queryset = Receipe.objects.get(id = id)

    if request.method == 'POST':
        data = request.POST

        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')

        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description

        if receipe_image:
            queryset.receipe_image = receipe_image

        queryset.save()
        return redirect('/')
    
    context = {'receipe':queryset}
    return render(request,'update_receipes.html',context)