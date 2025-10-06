from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.utils import timezone
from patients.models import Patient
from doctors.models import Doctor
from appointments.models import Appointment
from inventory.models import Medicine


def index(request):
    if request.user.is_authenticated:
        return redirect('core:dashboard')
    return render(request, 'core/index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def dashboard(request):
    today = timezone.now().date()
    
    # Get statistics
    total_patients = Patient.objects.count()
    total_doctors = Doctor.objects.count()
    total_medicines = Medicine.objects.count()
    today_appointments = Appointment.objects.filter(
        appointment_date=today
    ).count()
    
    # Get recent appointments
    recent_appointments = Appointment.objects.select_related(
        'patient__user', 'doctor__user'
    ).order_by('-appointment_date')[:10]
    
    context = {
        'today': today,
        'total_patients': total_patients,
        'total_doctors': total_doctors,
        'total_medicines': total_medicines,
        'today_appointments': today_appointments,
        'recent_appointments': recent_appointments,
    }
    
    return render(request, 'core/dashboard.html', context)