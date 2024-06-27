from django.shortcuts import render,redirect
from django.contrib.auth import login
from .forms import StudentSignupForm, ProfessorSignupForm
from .models import Student, Professor
# Create your views here.

def student_signup(request):
    if request.method == 'POST':
        form = StudentSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('student_home')
    else:
        form = StudentSignupForm()
    return render(request, 'student_signup.html', {'form': form, 'user_type': 'Student'})


def professor_signup(request):
    if request.method == 'POST':
        form = ProfessorSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('professor_home')
    else:
        form = ProfessorSignupForm()
    return render(request, 'professor_signup.html', {'form': form, 'user_type': 'Professor'})

