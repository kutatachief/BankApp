from django.contrib import admin
from .models import User, OTPCODE, PersonalAccount, BusinessAccount

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','username','email','phone','is_staff','is_superuser','created_at','email_verified','phone_verified']

@admin.register(PersonalAccount)
class  PersonalAccountAdmin(admin.ModelAdmin):
    list_display = ['user','date_of_birth','image']

@admin.register(BusinessAccount)
class BusinessAccountAdmin(admin.ModelAdmin):
    list_display = ['user','date_of_birth','company_name','registration_number','business_address','legal_name','logo']

@admin.register(OTPCODE)
class  OTPCODEAdmin(admin.ModelAdmin):
    list_display = ['user','email_otp','phone_otp','created_at',]

