from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Room, Topic
from .forms import RoomForm


def home(request):
    # Verificação para saber se está retornando algo
    q = request.GET.get('q') if request.GET.get('q') is not None else ''

    # Queremos ter certeza que iremos encontrar o valor passado
    # no topic name

    # icontains: para ignorar se é maiúscula ou minúscula
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )

    topics = Topic.objects.all()

    context = {'rooms': rooms, 'topics': topics}

    return render(request, 'base/home.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)


def createRoom(request):
    form = RoomForm()
    #  Se dermos um print no request.POST irá retornar
    # todos os dados armazenados na respectiva tabela
    if request.method == 'POST':
        # Add a data to the form
        form = RoomForm(request.POST)
        # Check the form
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)


def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)


def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.method == 'POST':
        room.delete()
        return redirect('home')

    return render(request, 'base/delete.html', {'obj': room})
