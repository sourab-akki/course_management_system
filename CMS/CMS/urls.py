from django.contrib import admin
from django.urls import path

from app.views import professor_courses,edit_student,students_list,professor_enrollments,professor_dashboard,add_course,enrollments_list,enroll_course,courses_list,professors_list,student_home,student_signup,professor_signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', student_signup, name='home'),
    path('signup/student/', student_signup, name='student_signup'),
    path('signup/professor/', professor_signup, name='professor_signup'),
    path('student/home/', student_home, name='student_home'),
    path('professor/home/', professor_dashboard, name='professor_home'),
    path('professors/', professors_list, name='professors_list'),
    path('courses/', courses_list, name='courses_list'),
    path('enroll/<int:course_id>/', enroll_course, name='enroll_course'),
    path('enrollments/', enrollments_list, name='enrollments_list'),
    path('add_course/', add_course, name='add_course'),
    path('professor/enrollments/', professor_enrollments, name='professor_enrollments'),
    path('professor/courses/', professor_courses, name='professor_courses'),
    path('students/', students_list, name='student_list'),
    path('student/edit/', edit_student, name='edit_student'),
]
