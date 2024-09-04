from django.shortcuts import render, HttpResponse, redirect
from .models import Room, Topic
from .forms import RoomForm

# Create your views here.
"""rooms = [
    {'id':1, 'name': 'lets learn python'},
    {'id':2, 'name': 'lets learn ruby'},
    {'id':3, 'name': 'lets learn django'},
    {'id':4, 'name': 'lets learn java'},
]
context = {'rooms':rooms}
"""

def home_view (request, *args, **kwargs):
    #return HttpResponse ("Welcome to the home page!!")
    topics = Topic.objects.all()
    rooms = Room.objects.all()
    context = {'topics':topics, 'rooms':rooms}
    return render (request, 'base/home.html', context) 
def room_view(request, pk, *args, **kwargs):
    room  = Room.objects.get(id=pk)
    context = {'room':room}
    """ for i in rooms:
        if i['id'] == int(pk):
            room = i
        context = {'room': room}"""
    return render (request, 'base/room.html', context)


def create_room(request, *args, **kwargs):
    form = RoomForm

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('home')
        #print(request.POST)
    context = {'form':form}
    return render(request, 'base/room_form.html', context)



def update_room(request, pk, *args, **kwargs):
    room= Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance = room)
        if form.is_valid():
            form.save()
            return redirect ('home')


    context = {'form':form}
    return render (request,'base/room_form.html', context)


def delete_room(request, pk, *args, **kwargs):
    room = Room.objects.get(id=pk)

    if request.method == "POST":
        room.delete()
        return redirect ('home')
    return render(request, 'base/delete.html', {'obj':room})


def search (request, *args, **kwargs):

    context = {}
    return render(request, 'base/.html', context)




