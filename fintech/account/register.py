from django.views import View
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterView(View):
    def get(self, request):
        return render(request, 'account/signup.html')
    

    def post(self, request):
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        account_type = request.POST.get('account_type')

        if not email or not phone or not username or not password or not password or not account_type:
            return JsonResponse({'error': 'All fields are required'}, status=400)  

        if password != password2:
            return JsonResponse({'error': 'Passwords do not match'}, status=400) 

        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Username already exist'}, status=400) 

        if User.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Email already exist'}, status=400) 

        if User.objects.filter(phone=phone).exists():
            return JsonResponse({'error': 'Phone already exist'}, status=400)

        # if User.objects.filter(password=password).exists():
        #     return JsonResponse({'error': 'Password already exist'}, status=400) 

        # Example: Create a new user
        user = User.objects.create_user(
             username=username,
             email=email,
             account_type=account_type,
             password=password
            ) 
      

    