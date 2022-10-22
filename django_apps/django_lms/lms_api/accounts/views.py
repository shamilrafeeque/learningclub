
# from accounts.serializers import MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import AccountSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView
#for admin 
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Account
from .serializers import AccountSerializer
from django.shortcuts import get_object_or_404


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        # token['name'] = user.name
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    
    
from rest_framework.views import APIView
class RegisterView(APIView):
    def post(self,request):
        data = request.data
        serializer = AccountSerializer(data=data)
        
        if serializer.is_valid():
                serializer.save()
                print("@@@@@*************************")
                print(serializer.data)

                response={
                    "messages" : "User Created Successfully",
                    "data" : serializer.data
                }
                
                return Response(data= response, status = status.HTTP_201_CREATED)
            
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
# from django.contrib.auth.hashers import make_password
# from .models import Account
# from  rest_framework.decorators import api_view,permission_classes
# @api_view(['POST'])
# def RegisterView(request):
#     data=request.data
#     email=data['email']
#     # email = request.POST.get('email')
#     # mobile = request.POST.get('mobile')
#     mobile=data['mobile']
#     if Account.objects.filter(email=email):
#         return Response('Email account already exists',status=status.HTTP_202_ACCEPTED)
#     elif Account.objects.filter(mobile=mobile):
#         return Response('Phone number already exists',status=status.HTTP_202_ACCEPTED)
#     else:
#         user = Account.objects.create(username=data['username'],
#         email=data['email'],
#         password=make_password(data['password']),
#         bio=data['bio'],
#         mobile=data['mobile'],
#         interests=data['interests'],
       
#     )
 
#     return Response(user)

@permission_classes([IsAuthenticated])
@api_view(['GET'])
def getAllUsers(request):
    users = Account.objects.filter(is_staff=False,is_superuser=False).order_by('id')
    serializer = AccountSerializer(users,many=True)
    return Response(serializer.data)


class AllUsers(APIView):
    # permission_classes=[IsAuthenticated]
    print("****************************")
    def patch(self,request,id):
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        user = get_object_or_404(Account,id=id)
        print("555555555555555555555")
        if user.is_active==True:
            user.is_active=False
            user.save()
            return Response({'is_activefirst step false':user.is_active})
        else:
            user.is_active=True
            user.save()
            return Response({'is_active':user.is_active})