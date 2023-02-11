from django import forms


class RegisterForm(forms.Form):

    username = forms.CharField(label="Nom d’utilisateur", min_length=5, max_length=100)
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Mot de passe ", min_length=10, max_length=100, widget=forms.PasswordInput())

    def clean(self):
        pass

    def clean_password(self):
        if self.cleaned_data['password'] == '':
            self.add_error('password', "password can't be empty!")
        return self.cleaned_data['password']

    def clean_username(self):
        if self.cleaned_data['username'] == '':
            self.add_error('username', "username can't be empty!")
        return self.cleaned_data['username']

    def clean_email(self):
        if self.cleaned_data['email'] == '':
            self.add_error('email', "email name can't be empty!")
        return self.cleaned_data['email']


