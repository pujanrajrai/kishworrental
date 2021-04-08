from django.shortcuts import render
from .forms import VehicleForms
from .models import Vehicle


# Create your views here.

def add_vehicle(request):
    if request.method == 'POST':
        forms = VehicleForms(request.POST, request.FILES)
        if forms.is_valid():
            vehicle = Vehicle(
                owner=request.user,
                name=request.POST.get('name'),
                km_driven=request.POST.get('km_driven'),
                seat=request.POST.get('seat'),
                price_per_day=request.POST.get('price_per_day'),
                wheeler=request.POST.get('wheeler'),
                transmission=request.POST.get('transmission'),
                type=request.POST.get('type'),
                details=request.POST.get('details'),
                number_plate=request.POST.get('number_plate'),
                vehicle=request.FILES['vehicle'],
            )
            vehicle.save()
        else:
            context = {"errors": forms.errors}
            return render(request, 'vehicle/add.html', context)

    return render(request, 'vehicle/add.html')
