from django.forms import ModelForm
from .models import Room


class RoomForm(ModelForm):
    class Meta:
        # Room --> model que iremos tirar como base
        # fields --> '__all__' (todos os campos)
        # exceção: aqueles que não temos controle (update e create)
        model = Room
        fields = '__all__'
