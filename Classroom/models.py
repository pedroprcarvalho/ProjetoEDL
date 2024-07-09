from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Instructor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)

class Classes(models.Model):
    name = models.CharField(max_length=100)
    code = models.IntegerField(unique=True)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 

    name = models.CharField(max_length=100)
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE)


class Assigments(models.Model):
    descricao = models.CharField(max_length=1000)
    turma = models.ForeignKey(Classes, on_delete=models.CASCADE)
    