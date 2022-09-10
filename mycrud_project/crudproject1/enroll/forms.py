from django.core import validators
from django import forms
from .models import User


class StudentRegistration(forms.ModelForm):
    class Meta:
      model = User
      fields = ['book_name', 'date', 'email', 'number']
      Widgets = {'book_name': forms.TextInput(attrs={'class':'form-control'}),
                 'date': forms.DateInput(attrs={'class':'form-control'}),
                 'email': forms.EmailInput(attrs={'class':'form-control'}),
                 'number': forms.NumberInput(attrs={'class':'form-control'}),
                }
