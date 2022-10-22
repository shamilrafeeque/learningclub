from django.urls import path
from . import views


urlpatterns = [
    path('teacher/', views.TeacherList.as_view()),
    path('teacher/<int:pk>/', views.TeacherDetail.as_view()),
    path('teacherlogin/',views.teacher_login),
    # path('admin/',views.AdminLogin.as_view()),
]