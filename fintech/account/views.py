from django.shortcuts import render
from .home import Index
from .register import RegisterView
from .login import LoginView

def otpverify(request):
    return render(request, 'account/otpverify.html')