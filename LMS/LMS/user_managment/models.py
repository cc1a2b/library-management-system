from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    class Meta:
        db_table = 'auth_user'

    def str(self):
        return self.username


class Genders(models.Model):
    id = models.IntegerField(primary_key=True)
    gender = models.CharField(max_length=30)
    gender_persian = models.CharField(max_length=30)


class Roles(models.Model):
    id = models.IntegerField(primary_key=True)
    role = models.CharField(max_length=50)
    role_persian = models.CharField(max_length=50)


class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    gender_id = models.ForeignKey(Genders, on_delete=models.CASCADE)
    faculty_id = models.ForeignKey("book_managment.Faculties", on_delete=models.CASCADE)
    email = models.EmailField(max_length=255)
    contact_no = models.CharField(max_length=14)
    identification_no = models.IntegerField(default=1)
    registration_no = models.IntegerField(default=1)
    page_no = models.IntegerField(default=1)
    original_address = models.CharField(max_length=255)
    username = models.CharField(max_length=50)
    usercard_address = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    role_id = models.ForeignKey(Roles, on_delete=models.CASCADE)
    is_active = models.CharField(max_length=1)
    signature = models.CharField(max_length=255)


class Depositories(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    copy_id = models.ForeignKey("book_managment.Copies", on_delete=models.CASCADE)
    issue_date = models.DateField()
    due_date = models.DateField()


class Semesters(models.Model):
    id = models.IntegerField(primary_key=True)
    semester = models.CharField(max_length=30)
    semester_persian = models.CharField(max_length=30)


class Cities(models.Model):
    id = models.IntegerField(primary_key=True)
    city = models.CharField(max_length=80)
    city_persian = models.CharField(max_length=80)


class Libraries(models.Model):
    id = models.IntegerField(primary_key=True)
    faculty_id = models.ForeignKey("book_managment.Faculties", on_delete=models.CASCADE)
    content = models.TextField()
    content_persian = models.TextField()
    privacy = models.TextField()
    privacy_persian = models.TextField()
    services = models.TextField()
    services_persian = models.TextField()
    email = models.EmailField(max_length=255)
