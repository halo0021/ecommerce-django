

from email.policy import default
from django.db import models

from django.contrib.auth.models import AbstractBaseUser , BaseUserManager

#Clase para crear un  usuario  o un super admin usuario
class MyAccountManager(BaseUserManager):
    def create_user(self,first_name,last_name,username,email,password=None):
        if not email:
        #si el usuario no ingresa el email disparara un error
            raise ValueError('el usuario debe tener un email')
        if not username:
             #si el usuario no ingresa el username disparara un error
            raise ValueError('el usuario debe tener un username')
        user=self.model(
              email=self.normalize_email(email),
              username= username,
              first_name= first_name,
              last_name= last_name,
             )

        user.set_password(password)
        user.save(using=self.db)
        return user  
    #funcion para crear un super usuario
    def create_superuser(self,first_name,last_name,email,username,password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username= username,
            password= password,
            first_name= first_name,
            last_name= last_name,
            
        )
        #estamos diciendo que el administrador tiene todo estos valores
        #activados por defecto
        user.is_admin=True
        user.is_active=True
        user.is_staff=True
        user.is_superadmin=True
        user.save(using=self._db)
        return user






class Account(AbstractBaseUser):
    first_name= models.CharField(max_length=50)
    last_name=models.CharField(max_length= 50)
    username= models.CharField(max_length=50, unique=True)
    email=  models.CharField(max_length=100, unique=True)
    phone_nuber=  models.CharField(max_length=50)

#campos de atributos de django

    date_joined = models.DateTimeField(auto_now_add=True)
    las_login = models.DateTimeField(auto_now_add=True)
    is_admin= models.BooleanField(default=False)
    is_staff= models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    is_superadmin=models.BooleanField(default=False)
    
#quiero que se inicie  con el email

    USERNAME_FIELD='email'
#campos obligatorios
    REQUIRED_FIELDS= ['username','first_name','last_name']
    
    #varaible para que se incluyan en el modelo account
    objects =MyAccountManager()
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.email
#saber que es  admin
    def has_perm(self, perm, obj=None):
        return self.is_admin
#dar acceso a los modulos
    def has_module_perms(self, add_label):
        return True



class UserProfile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    address_line_1 =  models.CharField(blank=True, max_length=100)
    address_line_2 =  models.CharField(blank=True, max_length=100)
    profile_picture = models.ImageField(blank=True, upload_to='userprofile')
    city = models.CharField(blank=True, max_length=20)
    state = models.CharField(blank=True, max_length=20)
    country = models.CharField(blank=True, max_length=20)

    def __str__(self):
        return self.user.first_name

    def full_address(self):
        return f'{self.address_line_1} {self.address_line_2}'