from django import forms

class RegisterForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=100)
    