from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self): return self.name

class Release(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField("date published")
    image = models.ImageField(upload_to='images/', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    def __str__(self): return self.name

one_to_ten_choices = [(i, i) for i in range(1, 11)]
class Comment(models.Model):
    release = models.ForeignKey(Release, on_delete=models.CASCADE, default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    text = models.TextField()
    text_grade = models.PositiveSmallIntegerField(choices=one_to_ten_choices, default=5, blank=True)
    charisma_grade = models.PositiveSmallIntegerField(choices=one_to_ten_choices, default=5, blank=True)
    realizationstyle_grade = models.PositiveSmallIntegerField(choices=one_to_ten_choices, default=5, blank=True)
    structurerhythm = models.PositiveSmallIntegerField(choices=one_to_ten_choices, default=5, blank=True)
    rate_grade = models.PositiveSmallIntegerField(choices=one_to_ten_choices, default=5, blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.release.name} - {self.text} - {self.text_grade} - {self.charisma_grade} - {self.structurerhythm} - {self.rate_grade}'

