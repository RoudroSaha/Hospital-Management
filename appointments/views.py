from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Appointment

def index(request):
    return render(request, "appointments/index.html")

@login_required
def appointment_list(request):
    appointments = Appointment.objects.all().order_by('-appointment_date')
    context = {
        'appointments': appointments,
    }
    return render(request, 'appointments/appointment_list.html', context)

@login_required
def appointment_detail(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    context = {
        'appointment': appointment,
    }
    return render(request, 'appointments/appointment_detail.html', context)

@login_required
def appointment_create(request):
    # TODO: Implement appointment creation form
    return render(request, 'appointments/appointment_form.html')

@login_required
def appointment_update(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    # TODO: Implement appointment update form
    context = {
        'appointment': appointment,
    }
    return render(request, 'appointments/appointment_form.html', context)

@login_required
def appointment_delete(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        appointment.delete()
        messages.success(request, 'Appointment deleted successfully!')
        return redirect('appointments:appointment_list')
    
    context = {
        'appointment': appointment,
    }
    return render(request, 'appointments/appointment_confirm_delete.html', context)
