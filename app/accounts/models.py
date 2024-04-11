from django.db import models
from django.contrib.auth.models import AbstractUser ,BaseUserManager
import datetime


GENDER = [("male","male"),("female","female")]
AVATAR = [("1","url 01"),("2","url 02")]
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have an password")
        
        email = self.normalize_email(str(email).strip().lower())
        username=f"{extra_fields.get("firstName")}.{extra_fields.get("lastName")}.{datetime.datetime.now().timestamp()}"
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        
        
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(
           email, password=password, **extra_fields)
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user
    
class profile(AbstractUser):
        
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['password','firstName','lastName']
    EMAIL_FIELD = 'email'

    objects = CustomUserManager()
    
    email = models.EmailField('email address', unique=True)
    password = models.CharField(blank=False,max_length=128, verbose_name='password')
    age = models.IntegerField(name='age',default=0)
    gender = models.CharField(choices=GENDER ,default="male")
    avatar = models.CharField(choices=AVATAR ,default="1")
    firstName= models.CharField(blank=False, max_length=150, verbose_name='first name')
    lastName = models.CharField(blank=False, max_length=150, verbose_name='last name')
    
    class Meta:
        app_label = 'accounts' 
        # constraints = [
        #     models.UniqueConstraint(fields=["email"], name="email_uniq")
        # ]
    
    def __str__(self) -> str:
        return f"first name:{self.firstName}, last name:{self.lastName} ,email: {self.email} "
    


        
