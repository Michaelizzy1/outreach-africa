from django.shortcuts import render, redirect
from .models import Photos, Message
from .forms import MessageForm

# Create your views here.


def index(request):
    images = Photos.objects.all()
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'images':images,
        'form': form
    }
    return render(request, 'missions/home.html', context)
