from django.shortcuts import render,get_object_or_404

from .models import Vehicle

# Create your views here.

def home(request):
    Vehicles =Vehicle.objects.all().filter(is_available=True)  #only seening in disply available item 
    context = {
        'Vehicles':Vehicles
    }
    return render(request, 'home.html',context)

def viewdetiles(request,car_id):
    cars= get_object_or_404(Vehicle,id=car_id)
    return render (request,'viewdetiles.html',{'car':cars})



    