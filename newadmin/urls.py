from django.urls import include, path
from .import views


urlpatterns = [
    path('admin_login',views.admin_login,name='admin_login'),
    path('user_deactivate/<int:id>',views.user_deactivate,name='user_deactivate'),
    path('user_activate/<int:id>',views.user_activate,name='user_activate'),
  
   
]
