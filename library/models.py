from django.db import models

# Create your models here.
class Author(models.Model):
    fname=models.CharField(max_length=100)
    lname= models.CharField(max_length=100)
    dob= models.DateField(null=True,blank=True)

    def __str__(self):
        return f'{self.fname},{self.lname}'

class Book(models.Model):
    title=models.CharField(max_length=250)
    author=models.ForeignKey(Author, on_delete=models.SET_NULL,null=True)
    isbn=models.CharField(max_length=13, unique=True)
    genre=models.CharField(max_length=50)
    available=models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} by {self.author}"