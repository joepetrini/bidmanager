from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models

class BidsUserManager(BaseUserManager):

    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email,
        favorite topping, and password.
        """
        if not email:
            msg = 'Users must have an email address'
            raise ValueError(msg)
        user = self.model(
            email=BidsUserManager.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email,
        favorite topping and password.
        """
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
class BidsUser(AbstractBaseUser, PermissionsMixin):
    """ Inherits from both the AbstractBaseUser and
    PermissionMixin.
    """
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        db_index=True,
    )
    USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = ['favorite_topping', ]
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    objects = BidsUserManager()
    
    def get_full_name(self):
        # The user is identified by their email and
        # favorite topping
        return "%s prefers %s" % (self.email)
        
    def get_short_name(self):
        # The user is identified by their email address
        return self.email
    
    def __unicode__(self):
        return self.email