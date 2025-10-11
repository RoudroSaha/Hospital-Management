from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.urls import reverse
from users.models import Doctors, Specialty, Patients
from patients.models import Appointment, Time, Status
from django.views.decorators.http import require_GET

User = get_user_model()


@login_required(login_url="/login")
def patient_dashboard(request):
    return render(request, "patients/patient_dashboard.html")


@login_required(login_url="/login")
def my_appointments(request):
    app = Appointment.objects.filter(patient__user=request.user)

    filter_status = request.GET.get("filter_status")
    filter_date = request.GET.get("filter_date")
    filter_doctor_name = request.GET.get("filter_doctor_name")

    if filter_status and filter_status != "All":
        app = app.filter(status__status=filter_status)

    if filter_date:
        app = app.filter(start_date=filter_date)

    if filter_doctor_name:
        app = app.filter(doctor__user__first_name__icontains=filter_doctor_name)

    return render(
        request,
        "patients/my_appointments.html",
        {
            "appointments": app,
            "filter_status": filter_status,
            "filter_date": filter_date,
            "filter_doctor_name": filter_doctor_name,
        },
    )


@login_required(login_url="/login")
def book_appointment(request):
    specialities = Specialty.objects.all()
    doctors = Doctors.objects.all()

    filter_speciality = request.GET.get("filter_speciality")
    filter_city = request.GET.get("filter_city")
    filter_doctor_name = request.GET.get("filter_doctor_name")

    if filter_speciality and filter_speciality != "All":
        doctors = doctors.filter(specialty__name=filter_speciality)

    if filter_doctor_name:
        doctors = doctors.filter(user__first_name__icontains=filter_doctor_name)

    if filter_city:
        doctors = doctors.filter(user__id_address__city__icontains=filter_city)

    return render(
        request,
        "patients/book_appointment.html",
        {
            "doctors": doctors,
            "specialities": specialities,
            "filter_speciality": filter_speciality,
            "filter_doctor_name": filter_doctor_name,
            "filter_city": filter_city,
        },
    )


@require_GET
def medishop(request):
    """Public medishop demo page with static products and client-side fake checkout."""
    # simple static list will be rendered in template
    return render(request, "medishop.html")
    # return render(request,'patients/book_appointment.html',{"doctors":doctors})


@login_required(login_url="/login")
def patient_confirm_book(request, doctor):
    print(doctor)
    if request.method == "POST":
        # Basic form values
        date = request.POST.get("date")
        summary = request.POST.get("summary")
        description = request.POST.get("description")
        time_value = request.POST.get("time")

        # Validate required fields
        if not date or not summary or not time_value:
            messages.error(request, "Please provide date, time and summary for the appointment.")
            return redirect(reverse("patient_confirm_book", args=[doctor]))

        try:
            heure = Time.objects.get(time=time_value)
        except Time.DoesNotExist:
            messages.error(request, "Selected time is not available.")
            return redirect(reverse("patient_confirm_book", args=[doctor]))

        try:
            doc = Doctors.objects.get(user__username=doctor)
        except Doctors.DoesNotExist:
            messages.error(request, "Doctor not found.")
            return redirect("book_appointment")

        try:
            patient = Patients.objects.get(user=request.user)
        except Patients.DoesNotExist:
            messages.error(request, "Patient profile not found.")
            return redirect("patient_dashboard")

        # Get or create a waiting status
        status, _ = Status.objects.get_or_create(status="Waited")

        # Prevent duplicate appointment for same doctor, date and time
        existing = Appointment.objects.filter(doctor=doc, start_date=date, time=heure)
        if existing.exists():
            messages.error(
                request,
                "The selected slot for this doctor is already booked. Please pick another date/time.",
            )
            return redirect(reverse("patient_confirm_book", args=[doctor]))

        appointment = Appointment.objects.create(
            summary=summary,
            description=description or "",
            start_date=date,
            time=heure,
            doctor=doc,
            patient=patient,
            status=status,
        )

        if appointment:
            messages.success(request, "Appointment booked successfully.")
            return redirect("my_appointments")

    try:
        doc = Doctors.objects.get(user__username=doctor)
    except Doctors.DoesNotExist:
        messages.error(request, "Doctor not found.")
        doctors = Doctors.objects.all()
        return render(request, "patients/book_appointment.html", {"doctors": doctors})

    times = Time.objects.all()
    return render(request, "patients/patient_confirm_book.html", {"times": times, "doctor": doc})
