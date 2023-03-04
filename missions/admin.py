from django.contrib import admin
from .models import Photos, Message, Sermon, Testimony, Event

# Register your models here.

admin.site.register(Photos)
admin.site.register(Message)
admin.site.register(Sermon)
admin.site.register(Testimony)
admin.site.register(Event)
