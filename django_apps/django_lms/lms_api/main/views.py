import email
from winreg import QueryValue
from django.shortcuts import render
from rest_framework.views import APIView
# from django_lms.lms_api.main.serializers import TeacherSerializer
from rest_framework.response import Response
from . import models
from .serializers import TeacherSerializer
from rest_framework import generics
# from rest_framework import  permissions
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Teacher
from rest_framework.decorators import api_view
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import status

# # Create your views here.
class TeacherList(generics.ListCreateAPIView):
#     # def get(self,request):
#     #     teachers=models.Teacher.objects.all()
#     #     serializer=TeacherSerializer(teachers,many=True)
#     #     return Response(serializer.data)
    queryset=models.Teacher.objects.all()
    serializer_class=TeacherSerializer
#     # permission_classes=[permissions.IsAuthenticated]
    
class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Teacher.objects.all()
    serializer_class=TeacherSerializer
#     # permission_classes=[permissions.IsAuthenticated]
# # @csrf_exempt
# # @api_view(['POST'])
# # def teacher_login(request):
# #     print('********************************')
# #     print(request)
# #     email=request.data['email']
# #     password=request.data['password']
# #     print(email)
# #     print(password)
    
# #     print("jjdjhjh")

# #     teacherdata=Teacher.objects.filter(email=email,password=password)
# #     print('hghdhghg')
# #     if teacherdata:
# #         print('dddddddd')
# #         return JsonResponse({'bool':True})
       
# #     else:
# #         return JsonResponse({'bool':False})
    
#     # except models.Teacher.DoesNotExist:
#     #     teacherdata=None
#     #     if teacherdata:
#     #         return JsonResponse({'bool':True})
#     #     else:
#     #         return JsonResponse({'bool':False})
@csrf_exempt
def teacher_login(request):
    print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^!!!!!!')
    # teacherData=Teacher.objects.filter(email="shh@gmail.com")
    try:
        email=request.POST['email']
        password=request.POST['password']
        teacherData=models.Teacher.objects.get(email=email,password=password)
        
        if teacherData:
            print('##########################')
            return JsonResponse({'bool':True})
        else:
            return JsonResponse({'bool':False})
    except:
        print("An exception occurred")
        return JsonResponse({'bool':False})
    

# class AccountList(APIView):
#     serializer_class = TeacherSerializer
#     @csrf_exempt
#     def post(self, request, format=None):
#             serializer = TeacherSerializer(data=request.data)
#             if serializer.is_valid():
#                 instance=serializer.save()
#                 instance.set_password(instance.password)
#                 instance.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    