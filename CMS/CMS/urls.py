from django.contrib import admin
from django.urls import path

from app.views import add_course,enrollments_list,enroll_course,courses_list,professors_list,student_home,student_signup,professor_signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/student/', student_signup, name='student_signup'),
    path('signup/professor/', professor_signup, name='professor_signup'),
    path('student/home/', student_home, name='student_home'),
    path('professors/', professors_list, name='professors_list'),
    path('courses/', courses_list, name='courses_list'),
    path('enroll/<int:course_id>/', enroll_course, name='enroll_course'),
    path('enrollments/', enrollments_list, name='enrollments_list'),
    path('add_course/', add_course, name='add_course'),
]
