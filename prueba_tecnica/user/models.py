from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin #mezcla de permisos

# Create your models here.
class UserManager(BaseUserManager): # class to create super user by django
    def create_user(self, email, password = None, **kwargs):
        if not email:
            raise TypeError("Users should have a email.")
        if not password:
            raise TypeError("Password should not be none.")
        
        user = self.model(email=self.normalize_email(email),**kwargs)
        user.set_password(password)
        
        user.save()
        return user
    
    def create_superuser(self, email, password=None, **kwargs):
        if not email:
            raise TypeError("Users should have a email.")
        if not password:
            raise TypeError("Password should not be none.")

        user = self.model(email=self.normalize_email(email), **kwargs)
        user.is_staff = True
        user.is_superuser=True
        user.email = email
        user.set_password(password)
        user.save()
        return user

class UserModel(AbstractBaseUser, PermissionsMixin): 

    email = models.EmailField(max_length = 50, unique = True)
    password = models.CharField(max_length = 9)
    
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)

    objects = UserManager() # here we create super user

    USERNAME_FIELD = "email"
    
    def __str__(self): # to show the email fr everytime this is invoked
        return self.email

    class Meta:
        db_table = 'user'