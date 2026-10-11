
import secrets

from django.shortcuts import render, redirect, get_object_or_404
from .models import Room


def home(request):
    if request.method == 'POST':
        room_code = secrets.token_urlsafe(16)

        room = Room.objects.create(
            room_code=room_code
        )

        return redirect('room', room_code=room.room_code)

    return render(request, 'rooms/home.html')


def room_detail(request, room_code):
    room = get_object_or_404(Room, room_code=room_code)

    return render(request, 'rooms/room.html', {
        'room': room
    })