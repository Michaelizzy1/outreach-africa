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


def testimony(request):
    form = TestimonyForm()
    if request.method == 'POST':
        form = TestimonyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('testimony')
    context = {
        'form': form
    }
    return render(request, 'missions/testimony.html', context)


def donate(request):
    return render(request, 'missions/donate.html')


def about(request):
    return render(request, 'missions/about.html')


def sermon(request):
    if 'q' in request.GET:
        q = request.GET['q']
        items = Sermon.objects.filter(Q(topic__icontains=q)
                                      | Q(speaker__icontains=q)
                                      | Q(location__icontains=q)
                                      )
    else:
        items = Sermon.objects.all()
        p = Paginator(items, 15)
        page_num = request.GET.get('page', 1)


        try:
            items = p.page(page_num)
        except EmptyPage:
            items = p.items(1)
    context = {
        'items': items,
    }
    return render(request, 'missions/sermons.html', context)


def discipleship(request):
    return render(request, 'missions/discipleship.html')


def media(request):
    items = Event.objects.all()
    context = {
        'items': items
    }

    return render(request, 'missions/media.html', context)


def contact(request):
    return render(request, 'missions/contact.html')


def download(request, id):
    items = Sermon.objects.get(id=id)
    context = {
        'topic': items.topic,
        'sermon': items.sermon,
        'location': items.location,
        'speaker': items.speaker,
    }
    return render(request, 'missions/download.html', context)