from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/',views.RegisterView.as_view(),name='register'),
    path('allusers/',views.getAllUsers),
    path('admin_panel/users/<int:id>/',views.AllUsers.as_view()),
    #  path('register/',views.RegisterView,name='signup'),
    # path('user/', views.UserList.as_view()),

    ]


urlpatterns = format_suffix_patterns(urlpatterns)