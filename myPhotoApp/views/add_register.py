from django.contrib.auth.models import User
from django.core.checks import messages
from django.urls import reverse
from django.views import generic
from myPhotoApp.forms.register_form import RegisterForm
from django.contrib import messages


class RegisterFormView(generic.FormView):
    template_name = 'register_new.html'
    form_class = RegisterForm

    def form_valid(self, form):

        email = form.cleaned_data['email']
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        try:
            User.objects.create_user(username=username, email=email, password=password)
            messages.add_message(self.request, messages.INFO, 'User created successfully')

        except Exception as e:
            form.add_error(None, "Unexpected error")
            return super().form_invalid(form)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('gallerie')
