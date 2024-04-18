from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    user_id = models.CharField(max_length=10)
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=12, blank=True, null=True)
    whatsapp = models.CharField(max_length=12, blank=True, null=True)
    # dob = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='profile_pic/', blank=True, null=True)
    updated_datetime = models.DateTimeField(auto_now=True)
    #TODO added address
    # address = models.ForeignKey(Address, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return f"{self.user_id}-{self.full_name}"


class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=100, blank=True, null=True)
    #TODO added responsibility
    # responsibility = models.ForeignKey(Responsibility, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return f"Teacher: {self.user}"


class Parent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    relation = models.CharField(max_length=100, blank=True, null=True)
    occupation = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self) -> str:
        return f"Parent: {self.user}"


class Standard(models.Model):
    short_form = models.CharField(max_length=5)
    full_form = models.CharField(max_length=150, blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    in_charge = models.ForeignKey(Teacher, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self) -> str:
        return f"Std: {self.short_form}"


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    standard = models.ForeignKey(Standard, on_delete=models.SET_NULL, blank=True, null=True)
    murshid = models.ForeignKey(Teacher, on_delete=models.SET_NULL, blank=True, null=True)
    parent = models.ForeignKey(Parent, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self) -> str:
        return f"Student: {self.user}"
