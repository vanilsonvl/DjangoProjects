from django.shortcuts import render, redirect, get_object_or_404

from app.models import Car
from .forms import CarForm


def register_car(request, template_name='car/car_form.html'):
    form = CarForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_carros')
    return render(request, template_name, {'form': form})


def car_list(request, template_name='car/car_list.html'):
    query = request.GET.get('buscar')
    if query:
        cars = Car.objects.filter(model__iexact=query)
    else:
        cars = Car.objects.all()
    return render(request, template_name, {'cars': cars})


def edit_car(request, pk, template_name='car/car_form.html'):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('lista_carros')
    else:
        form = CarForm(instance=car)
    return render(request, template_name, {'form': form})


def remove_car(request, pk, template_name='car/car_delete.html'):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        car.delete()
        return redirect('lista_carros')
    return render(request, template_name, {'car': car})