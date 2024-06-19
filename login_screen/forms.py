from django import forms

class LoginForm(forms.Form):
    code = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your login code'
    }))
