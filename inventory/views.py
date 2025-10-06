# inventory/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Medicine
from .forms import MedicineForm

@login_required
def inventory_list(request):
    medicines = Medicine.objects.all().order_by('name')
    context = {
        'medicines': medicines,
    }
    return render(request, 'inventory/inventory_list.html', context)

@login_required
def inventory_detail(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)
    context = {
        'medicine': medicine,
    }
    return render(request, 'inventory/inventory_detail.html', context)

@login_required
def inventory_create(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Medicine added successfully!')
            return redirect('inventory:inventory_list')
    else:
        form = MedicineForm()
    
    context = {
        'form': form,
        'title': 'Add Medicine',
    }
    return render(request, 'inventory/inventory_form.html', context)

@login_required
def inventory_update(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)
    
    if request.method == 'POST':
        form = MedicineForm(request.POST, instance=medicine)
        if form.is_valid():
            form.save()
            messages.success(request, 'Medicine updated successfully!')
            return redirect('inventory:inventory_detail', pk=medicine.pk)
    else:
        form = MedicineForm(instance=medicine)
    
    context = {
        'form': form,
        'medicine': medicine,
        'title': 'Update Medicine',
    }
    return render(request, 'inventory/inventory_form.html', context)

@login_required
def inventory_delete(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)
    
    if request.method == 'POST':
        medicine.delete()
        messages.success(request, 'Medicine deleted successfully!')
        return redirect('inventory:inventory_list')
    
    context = {
        'medicine': medicine,
    }
    return render(request, 'inventory/inventory_confirm_delete.html', context)
