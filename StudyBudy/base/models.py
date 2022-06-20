from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    model = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # Especificando a relação entre room e topic
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # participants
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# https://docs.djangoproject.com/en/4.0/ref/contrib/auth/

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # ForeignKey --> permite a conexão com outra classe
    # CASCADE --> quando deletado, deleta todos os descendentes
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # retorna os 50 primeiros caracteres
        return self.body[0:50]
