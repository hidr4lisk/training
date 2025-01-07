from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login:login')

    def form_valid(self, form):
        messages.success(self.request, 'Cuenta creada exitosamente.')
        return super().form_valid(form)