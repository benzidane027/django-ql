from django.db import models
from django.contrib.auth.models import AbstractUser ,BaseUserManager
import datetime
import uuid

GENDER = [("male","male"),("female","female")]
AVATAR = [("1","url 01"),("2","url 02")]

def picture_upload(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(instance.image_uid, ext)
    folder_name= f"storeFolder_{instance.username.replace(".","_")}"
    
    return f"{folder_name}/{filename}"

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have an password")
        
        email = self.normalize_email(str(email).strip().lower())
        username=f"{extra_fields.get("first_name")}.{extra_fields.get("last_name")}.{datetime.datetime.now().timestamp()}"
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
    REQUIRED_FIELDS = ['password','first_name','last_name']
    EMAIL_FIELD = 'email'
    
    objects = CustomUserManager()
    image=models.ImageField("image","image",upload_to=picture_upload)
    image_uid = models.UUIDField(default=uuid.uuid4)
    
    email = models.EmailField('email address', unique=True)
    password = models.CharField(blank=False,max_length=128, verbose_name='password')
    age = models.IntegerField(name='age',default=0)
    gender = models.CharField(choices=GENDER ,default="male")
    avatar = models.CharField(choices=AVATAR ,default="1")
    first_name= models.CharField(blank=False, max_length=150, verbose_name='first name')
    last_name = models.CharField(blank=False, max_length=150, verbose_name='last name')
    
    @property
    def full_name(self):
        return f"{self.first_name}_{self.last_name}"
    
    class Meta:
        app_label = 'accounts' 
        # constraints = [
        #     models.UniqueConstraint(fields=["email"], name="email_uniq")
        # ]
    
    def __str__(self) -> str:
        return f"first name:{self.first_name}, last name:{self.last_name} ,email: {self.email} "
    


        
