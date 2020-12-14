from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,
BaseUserManager
)
class UserManager(BaseUserManager):
    def create_user(self, username, email, Full_name, password = None):
        if not username:
            raise ValueError("Por favor insira um nome de usuário")
        if not password:
            raise ValueError("O campo senha é de preenchimento obrigatório")
        if not email:
            raise ValueError("Por favor insira um email")
        if not Full_name:
            raise ValueError("Por favor insira um nome")
        
        user_obj = self.model(
            username=self.model.normalize_username(username),
            email = self.normalize_email(email),
            Full_name = Full_name,
            )

        user_obj.set_password(password)
        user_obj.active = True 
        user_obj.admin = False
        user_obj.staff = False
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self,username, email, Full_name, password):
        user = self.create_user(
            username,
            email,
            Full_name,
            password=password,
        )

        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self,username, email, Full_name, password):
        user = self.create_user(
            username,
            email,
            Full_name,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=120, unique=True)
    email = models.EmailField(unique=True, blank = True)
    Full_name = models.CharField(max_length=120, unique=True, blank = True)
    active = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS  = ['email', 'Full_name']

    objects = UserManager()
    def get_full_name(self):
        # The user is identified by their email address
        return self.Full_name

    def get_short_name(self):
        # The user is identified by their email address
        return self.Full_name

    def get_email(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active
