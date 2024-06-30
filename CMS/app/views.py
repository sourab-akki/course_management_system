from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login
from .forms import StudentSignupForm, ProfessorSignupForm,CourseForm,EditStudentForm
from .models import Student, Professor,Course,Enrollment
from django.utils import timezone


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

def edit_student(request):
    student = request.user
    print("student",student.username)
    if request.method == 'POST':
        form = EditStudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_home')  # Redirect to student home after successful update
    else:
        form = EditStudentForm(instance=student)
    return render(request, 'edit_student.html', {'form': form})

def professor_signup(request):
    if request.method == 'POST':
        form = ProfessorSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('professor_home')
    else:
        form = ProfessorSignupForm()
    return render(request, 'professor_signup.html', {'form': form, 'user_type': 'Professor'})


def student_home(request):
    student = request.user
    return render(request, 'home.html', {'student': student})


def professors_list(request):
    professors = Professor.objects.all()
    return render(request, 'professors_list.html', {'professors': professors})

def students_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})
def courses_list(request):
    courses = Course.objects.all()
    return render(request, 'courses_list.html', {'courses': courses})


def enroll_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    Enrollment.objects.create(student=request.user, course=course, date_enrolled=timezone.now().date())
    return redirect('student_home')

def enrollments_list(request):
    enrollments = Enrollment.objects.filter(student=request.user)
    return render(request, 'enrollments_list.html', {'enrollments': enrollments})

def professor_dashboard(request):
    professor = Professor.objects.get(user=request.user)
    return render(request, 'professor_dashboard.html', {'professor': professor})

def professor_enrollments(request):
    professor = Professor.objects.get(user=request.user)
    enrollments = Enrollment.objects.filter(course__professor=professor)
    return render(request, 'professor_enrollments.html', {'enrollments': enrollments})

def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.professor = Professor.objects.get(user=request.user)
            course.save()
            return redirect('professor_home')
    else:
        form = CourseForm()
    return render(request, 'add_course.html', {'form': form})