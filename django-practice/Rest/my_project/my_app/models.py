from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

class Cohort(models.Model):
    name = models.CharField(max_length=200)
    created =models.DateTimeField(auto_now_add=True)
    tag = models.CharField(max_length=5, null=True, blank=True)
    description = models.TextField(blank=True, null=True)