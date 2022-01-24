from django import forms


class RegistrationForm(forms.Form):  # Django is inferring this form from class 'Participant'
    email = forms.EmailField(label='Your email')

