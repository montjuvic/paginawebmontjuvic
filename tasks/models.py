from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Task(models.Model):

    titulo= models.CharField(max_length=100)
    description=models.TextField(blank=True)
    created=models.DateTimeField(auto_now_add=True)
    datecompleted=models.DateTimeField(null=True, blank=True)
    important=models.BooleanField(default=False)
    user=models.ForeignKey(User, on_delete=models.CASCADE) #Enlazamiento

    def __str__(self):

        return self.titulo + ' - by ' + self.user.username #sirve para mostrar el nombre del title en vez del task (1)