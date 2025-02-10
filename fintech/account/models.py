from django.db import models
from django.contrib.auth.models import AbstractUser
from shortuuid.django_fields import ShortUUIDField
from django.utils.timezone import now
from datetime import timedelta

ACCOUNT_TYPE_CHOICES = [
        ('personal', 'Personal'),
        ('business', 'Business'),
]
class User(AbstractUser):
    id = ShortUUIDField(primary_key=True, unique=True, editable=False, alphabet='bcarem12345qop09867890')
    username = models.CharField(max_length=200)
    phone = models.CharField(max_length=200, unique=True)
    email = models.EmailField(max_length=200,unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    email_verified = models.BooleanField(default=False)
    phone_verified = models.BooleanField(default=False)

    account_type = models.CharField(
        max_length=10,
        choices=ACCOUNT_TYPE_CHOICES,
        default='CUSTOMER'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone']

    def __str__(self):
        return self.username
    

class PersonalAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='personalaccount')
    date_of_birth = models.DateField()
    image = models.ImageField(upload_to='profile')

    def __str__(self):
        return self.user.username
    
    
class BusinessAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='businessaccount')
    date_of_birth = models.DateField()
    company_name = models.CharField(max_length=200)
    registration_number = models.CharField(max_length=200)
    business_address = models.TextField()
    legal_name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='business_logos', null=True, blank=True )

    def __str__(self):
        return self.user.username

class OTPCODE(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='otps')
    email_otp = models.CharField(max_length=6, null=True, blank=True)
    phone_otp = models.CharField(max_length=6, null=True, blank=True )
    created_at = models.DateTimeField(auto_now_add=True)

    def is_otps_expired(self):
        if self.created_at is None:
            return True
        return now() > self.created_at + timedelta(minutes=5)
    def __str__(self):
        return self.user.email