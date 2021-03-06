from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from appointments.models.appointment import Appointment

class AppointmentListView(ListView):
    model = Appointment
    template_name = 'appointments/appointments.html'
    paginate_by = 25

    def get_queryset(self):
        return self.model.objects.all()

class AppointmentCreateView(CreateView):
    model = Appointment
    fields = ('patient', 'doctor', 'appointment_type', 'start_time', 'end_time', 'details')
    template_name = 'appointments/appointment_form.html'
    success_url = reverse_lazy('appointments')

class AppointmentUpdateView(UpdateView):
    model = Appointment
    fields = ('patient', 'doctor', 'appointment_type', 'start_time', 'end_time', 'details')
    template_name = 'appointments/appointment_form.html'
    success_url = reverse_lazy('appointments')

class AppointmentDeleteView(DeleteView):
    model = Appointment
    template_name = 'appointments/appointment_confirm_delete.html'
    success_url = reverse_lazy('appointments')