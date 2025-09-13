from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    class Meta:
        permissions = [
            ("can_view", "can view book"),
            ("can_create", "can add a book"),
            ("can_edit", "can edit book information"),
            ("can_delete", "can delete a book"),
        ]


class CustomUserManager(BaseUserManager):

    def create_user(self, username, email, password=None, date_of_birth=None, profile_photo=None, **extra_fields):

        if not username:
            raise ValueError("The Username field is required")

        if not email:
            raise ValueError("The Email field is required")

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, 
            date_of_birth=date_of_birth, profile_photo=profile_photo, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self, username, email, password=None, date_of_birth=None, profile_photo=None, **extra_fields):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")


        return self.create_user(
                username=username,
                email=email,
                password=password,
                date_of_birth=date_of_birth,
                profile_photo=profile_photo,
                **extra_fields
            )



class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to="profiles/", null=True, blank=True)

    objects = CustomUserManager()