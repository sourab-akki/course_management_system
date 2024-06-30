from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import Student,Professor,Course

class StudentSignupForm(UserCreationForm):
    address = forms.CharField(widget=forms.Textarea)
    phone_number = forms.CharField(max_length=15)

    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'email', 'address', 'phone_number', 'password1')

    def __init__(self, *args, **kwargs):
        super(StudentSignupForm, self).__init__(*args, **kwargs)
        self.fields.pop('password2')
        self.fields['phone_number'].label = "Phone Number (Username)"

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if Student.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError("A user with that phone number already exists.")
        return phone_number


class EditStudentForm(UserChangeForm):
    password = None

    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'email', 'address', 'phone_number')



class ProfessorSignupForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ('last_name', 'first_name', 'email', 'department')


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'description', 'credits']
