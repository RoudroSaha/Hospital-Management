from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Patient

@login_required
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patients/patient_list.html', {'patients': patients})