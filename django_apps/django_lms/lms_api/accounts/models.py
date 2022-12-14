# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# class UserAccountManager(BaseUserManager):
#     def create_user(self, email, name, password=None):
#         if not email:
#             raise ValueError('Users must have an email address')
        
#         email = self.normalize_email(email)
#         user = self.model(email=email, name=name)

#         user.set_password(password)
#         user.save()

#         return user
    
#     def create_superuser(self, email, name, password):
#         user = self.create_user(email, name, password)

#         user.is_superuser = True
#         user.is_staff = True
#         user.save(using=self._db)

#         return user

# class UserAccount(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(max_length=255, unique=True)
#     name = models.CharField(max_length=255)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)

    
    
#     username=models.CharField(max_length=233)
#     password=models.CharField(max_length=20)
#     bio=models.CharField(max_length=233)
#     mobile=models.IntegerField()
#     interests=models.CharField(max_length=255)
    
#     # last_login=models.DateTimeField(auto_now_add=True)
#     # joined_date=models.DateTimeField(auto_now_add=True)

#     objects = UserAccountManager()
    
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['name']

#     def get_full_name(self):
#         return self.name
    
#     def get_short_name(self):
#         return self.name
    
#     def __str__(self):
#         return self.email
    
    
from unicodedata import category
from django.db import models

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

from datetime import datetime
# Create your models here.
"""Custom user model Start"""


class MyAccountManager(BaseUserManager):
    def create_user(self,email,password=None):
        if not email:
            raise ValueError('Please Enter Email')
        if not password:
            raise ValueError('Please Enter Password')
        user=self.model(
            email  =  self.normalize_email(email),

        )
        user.is_active=True
        user.is_staff=False
        user.is_superuser=False
        user.is_verified=False
        user.set_password(password)
        user.save(using=self._db)
        return user
    


    def create_superuser(self,email,password):
        user=self.create_user(
            email=self.normalize_email(email),
            password=password
        )
       
        user.is_active=True
        user.is_staff=True
        user.is_superuser=True
        user.is_verified=True
        user.set_password(password)
        user.save(using=self._db)
        return user



class Account(AbstractBaseUser):
    username        =models.CharField(max_length=50)
    email           =models.EmailField(max_length=100,unique=True)   
    mobile          =models.CharField(max_length=10,unique=True,null=True)
    password        =models.CharField(max_length=220,blank=False,null=False)
    dp              =models.ImageField(upload_to='photos/users_dp/',blank=True)
    bio             =models.TextField(blank=True,null=True)
    interests       =models.TextField(max_length=1000,null=True,blank=True)
    wallet_balance  =models.IntegerField(default=0)
    account_holder_name =models.CharField(max_length=200,null=True,blank=True)
    bank            =models.CharField(max_length=200,null=True,blank=True)
    acc             =models.CharField(max_length=20,null=True,blank=True)
    ifsc            =models.CharField(max_length=20,null=True,blank=True)
    courses_created =models.IntegerField(default=0)
    courses_enrolled=models.IntegerField(default=0)
    
    
    joined_date     =models.DateTimeField(auto_now_add=True)
    last_login      =models.DateTimeField(auto_now=True)
    is_staff        =models.BooleanField(default=False)
    is_active       =models.BooleanField(default=True)
    is_verified     =models.BooleanField(default=False)
    is_superuser   =models.BooleanField(default=False)

    USERNAME_FIELD  ='email'
    REQUIRED_FIELDS =['password']
    
    objects=MyAccountManager()

    def get_date(self):
        time = datetime.now()
        if self.joined_date.day == time.day:
            return str(time.hour - self.joined_date.hour) + " hours ago"
        else:
            if self.joined_date.month == time.month:
                return str(time.day - self.joined_date.day) + " days ago"
            else:
                if self.joined_date.year == time.year:
                    return str(time.month - self.joined_date.month) + " months ago"
        return self.joined_date

    def __str__(self):
        return self.email
    def has_perm(self,perm,obj=None):
        return self.is_superuser
    def has_module_perms(self,add_label):
        return True
    
    