from django.urls import include, path
from .import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
   path('',views.login,name='login'),
   path('register',views.register,name='register'),
   path('login_sub',views.login_sub,name='login_sub'),
   path('user_view',views.user_view,name='user_view'),
   path('logout',views.logout,name='logout'), 
]
