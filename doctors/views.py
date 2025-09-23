from django.shortcuts import render

def index(request):
    return render(request, "doctors/index.html")

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, "doctors/doctor_list.html", {"doctors": doctors})
