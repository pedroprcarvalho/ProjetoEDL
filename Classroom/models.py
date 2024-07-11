from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Dados(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length = 11, unique=True)
    matricula = models.CharField(max_length=10, unique=True)
    nome = models.CharField(max_length = 20)
    email = models.CharField(max_length=100)
    nota1 = models.IntegerField()
    nota2 = models.IntegerField()


    def __str__(self):
        return self.nome