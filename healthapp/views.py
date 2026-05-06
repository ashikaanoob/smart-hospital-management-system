
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Doctor,Patient,Appointment
from .forms import DoctorForm, PatientForm, AppointmentForm


def home(request):
    doctor_count = Doctor.objects.count()
    patient_count = Patient.objects.count()
    appointment_count = Appointment.objects.count()

    context = {
        'doctor_count': doctor_count,
        'patient_count': patient_count,
        'appointment_count': appointment_count,
    }

    return render(request, 'home.html', context)

def doctor_list(request):
    query = request.GET.get('q')
    doctors = Doctor.objects.all()

    if query:
        doctors = doctors.filter(name__icontains=query)

    return render(request, 'doctor_list.html', {'doctors': doctors})


def add_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Doctor added successfully!')
            return redirect('doctor_list')
    else:
        form = DoctorForm()
    return render(request, 'doctor_form.html', {'form': form})


def edit_doctor(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    form = DoctorForm(request.POST or None, instance=doctor)
    if form.is_valid():
        form.save()
        messages.success(request, 'Doctor updated successfully!')
        return redirect('doctor_list')
    return render(request, 'doctor_form.html', {'form': form})


def delete_doctor(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    doctor.delete()
    messages.success(request, 'Doctor deleted successfully!')
    return redirect('doctor_list')



def patient_list(request):
    query = request.GET.get('q')
    patients = Patient.objects.all()

    if query:
        patients = patients.filter(name__icontains=query)

    return render(request, 'patient_list.html', {'patients': patients})

def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Patient added successfully!')
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'patient_form.html', {'form': form})


def edit_patient(request, id):
    patient = get_object_or_404(Patient, id=id)
    form = PatientForm(request.POST or None, instance=patient)
    if form.is_valid():
        form.save()
        messages.success(request, 'Patient updated successfully!')
        return redirect('patient_list')
    return render(request, 'patient_form.html', {'form': form})


def delete_patient(request, id):
    patient = get_object_or_404(Patient, id=id)
    patient.delete()
    messages.success(request, 'Patient deleted successfully!')
    return redirect('patient_list')



def appointment_list(request):
    query = request.GET.get('q')
    appointments = Appointment.objects.all()

    if query:
        appointments = appointments.filter(patient__name__icontains=query)

    return render(request, 'appointment_list.html', {'appointments': appointments})


def add_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Appointment added successfully!')
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'appointment_form.html', {'form': form})


def edit_appointment(request, id):
    appointment = get_object_or_404(Appointment, id=id)
    form = AppointmentForm(request.POST or None, instance=appointment)
    if form.is_valid():
        form.save()
        messages.success(request, 'Appointment updated successfully!')
        return redirect('appointment_list')
    return render(request, 'appointment_form.html', {'form': form})


def delete_appointment(request, id):
    appointment = get_object_or_404(Appointment, id=id)
    appointment.delete()
    messages.success(request, 'Appointment deleted successfully!')
    return redirect('appointment_list')