from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self): return self.name

class Release(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField("date published")
    image = models.ImageField(upload_to='images/', blank=True) #'images/%Y/%m/%d/'
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    def __str__(self): return self.name
    
class Comment(models.Model):
    release = models.ForeignKey(Release, on_delete=models.CASCADE, default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    text = models.TextField()

    def __str__(self):
        return f'{self.user.username} - {self.release.name} - {self.text}'

