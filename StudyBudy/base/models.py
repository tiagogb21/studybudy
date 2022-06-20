from django.db import models


class Room(models.Model):
    # host
    # topic
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # participants
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    # user =
    # ForeignKey --> permite a conexão com outra classe
    # CASCADE --> quando deletado, deleta todos os descendentes
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # retorna os 50 primeiros caracteres
        return self.body[0:50]
