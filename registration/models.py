from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# For profile which includes photo and username
# class Profile(models.Model):
#   user = models.OneToOneField(User, on_delete=models.CASCADE)
#   image = models.ImageField(default='default.jpg', upload_to='profile_pics')

# def __str__(self):
# return f'{self.user.username} Profile'

# def save(self):
# super().save()

#img = Image.open(self.image.path)

# if img.height > 300 or img.width > 300:
#   output_size = (300, 300)
#   img.thumbnail(output_size)
#   img.save(self.image.path)


class Mentor(models.Model):
    mentor_id = models.CharField(max_length=10)
    gender = models.CharField(default="Male", max_length=10)
    year = models.CharField(max_length=20, default="2018")
    department = models.CharField(max_length=100, default="Civil")
    degree = models.CharField(max_length=100, default="BTech")
    city = models.CharField(max_length=100, default="Mumbai")
    country = models.CharField(max_length=100, default="India")
    designation = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    discp = models.TextField(blank=True)
    interest = models.CharField(max_length=200, null=True)
    maxmentees = models.IntegerField(default=0)
    score = models.FloatField(default=0.0)
    available = models.BooleanField(default=True)
    maxscore = models.FloatField(default=0.0)
    favourites = models.ManyToManyField(
        User, related_name='favourite', default=None, blank=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    password = models.CharField(max_length=20)
    fullname = models.CharField(max_length=100, blank=True)
    rollno = models.CharField(max_length=100, blank=True)
    department = models.CharField(max_length=100, blank=True)
    degree = models.CharField(max_length=100, blank=True)
    contactno = models.CharField(max_length=100, blank=True)
    personalEmail = models.CharField(max_length=100, blank=True, default="")
    sop = models.CharField(max_length=500, blank=True)
    linkedin = models.CharField(max_length=100, blank=True)
    experience = models.CharField(max_length=500, blank=True)
    goal = models.CharField(max_length=500, blank=True)
    obstacle = models.CharField(max_length=500, blank=True)
    pref_1 = models.IntegerField(blank=True, null=True)
    pref_2 = models.IntegerField(blank=True, null=True)
    pref_3 = models.IntegerField(blank=True, null=True)
    pref_4 = models.IntegerField(blank=True, null=True)
    pref_5 = models.IntegerField(blank=True, null=True)
    # submitted = models.BooleanField(default=False)
