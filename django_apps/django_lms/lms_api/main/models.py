from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
# Create your models here.
class Teacher(models.Model):
    full_name=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    password=models.CharField(max_length=255)
    qualification=models.CharField(max_length=255)
    mobile_no=models.CharField(max_length=255)
    skills=models.TextField(max_length=250)
    
    
    def __str__(self):
        return self.full_name
    
# class CourseCategory(models.Model):
#     title=models.CharField(max_length=255)
#     description=models.TextField()
    
#     class Meta:
#         verbose_name_plural='Course Categories'
    
# class Course(models.Model):
#     # category=models.ForeignKey(CourseCategory,on_delete=models.CASCADE)
#     # teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
#     title=models.CharField(max_length=255)
#     description=models.TextField()
    
#     # 
# class Student(models.Model):
#     full_name=models.CharField(max_length=255)
#     email=models.CharField(max_length=255)
#     password=models.CharField(max_length=255)
#     qualification=models.CharField(max_length=255)
#     mobile_no=models.CharField(max_length=255)
#     address=models.TextField()
#     interested_categories=models.CharField(max_length=255)
    
# class UserAccountManager(BaseUserManager):
#     def create_user(self,email,name,password=None):
#         if not email:
#             raise ValueError("please enter email address")
#         if not name:
#             raise ValueError("please enter a name")
#         if not password:
#             raise ValueError("please enter password")
        
    
# class UserAccount(AbstractBaseUser):
#     email=models.EmailField(max_length=233,unique=True)
#     name=models.CharField(max_length=250)
#     is_active=models.BooleanField(default=True)
#     is_staff=models.BooleanField(default=False)
    
#     object=UserAccountManager()
    
#     def get_full_name(self):
#         return self.name
    
#     def get_short_name(self):
#         return self.name
