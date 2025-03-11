from .models import OTPCODE
from django.views.generic import View
from django.http import JsonResponse
from .models import User, OTPCODE
from .mailer_otpsender import send_otp
from django.shortcuts import render


class Email_VerificationView(View):
    def get(self,request):
        return render(request, 'lecbank/otpverify.html')
    
    def post(self,request):
        otp_user = request.POST.get("otp_code")

        if not otp_user:
            return JsonResponse({'error': "verification code is not provided"}, status=400)
        
        try:
            user_otp_records = OTPCODE.objects.get(email_otp=otp_user)

            # the user that want to verify their otp
            user = user_otp_records.user
        except OTPCODE.DoesNotExist:
            return JsonResponse({'error': "invalid verification code"}, status=400)
        
        if user_otp_records.is_otp_expired():
            send_otp(user.email)
            return JsonResponse({"error": "Code expired. A new code has been sent to your email"}, status=400)

        if user.email_verifiied:
            return JsonResponse({"error:" "Email already verified"}, status=400)
        
        user.email_verifiied = True
        user.save()
        return JsonResponse({"success": "Email verified successfully"}, status=200)










