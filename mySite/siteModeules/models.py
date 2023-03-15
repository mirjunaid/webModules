from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create Home Page models here.
class Module(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()

# End of calculator models.

# Create your calculator models here.
class SmartCalculator(models.Model):
    title= models.CharField(max_length=200)
    definition= models.TextField()
    formulas = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# End of calculator models.

# Create your Blog models here
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    