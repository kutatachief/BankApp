from django.urls import path
from . import views
from .home import Index
from .register import RegisterView
from .login import LoginView


urlpatterns = [
   path('', Index.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', RegisterView.as_view(), name='signup'),
    path('otpverify/', views.otpverify, name='otpverify'), 
   
]
