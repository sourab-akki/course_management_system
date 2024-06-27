from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Student,Professor

class StudentSignupForm(UserCreationForm):
    address = forms.CharField(widget=forms.Textarea)
    phone_number = forms.CharField(max_length=15)

    class Meta:
        model = Student
        fields = ('username', 'first_name', 'last_name', 'email', 'address', 'phone_number', 'password1', 'password2')


class ProfessorSignupForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ('last_name', 'first_name', 'email', 'department')

