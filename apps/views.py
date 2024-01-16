from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from apps.forms import RegisterForm
from apps.mixins import NotLoginRequiredMixin
from apps.models import Trener
from django.views.generic import ListView

class StaffListView(ListView):
    template_name = 'list.html'
    queryset = Trener.objects.all()
    context_object_name = 'staffs'

class CustomLoginView(NotLoginRequiredMixin, LoginView):
    template_name = 'login.html'

class RegisterFormView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('register_page')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
