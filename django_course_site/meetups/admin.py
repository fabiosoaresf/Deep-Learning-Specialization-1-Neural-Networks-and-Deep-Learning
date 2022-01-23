from django.contrib import admin

from .models import Meetup, Location, Participant

# Register your models here.


class MeetupAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'location', 'description')
    list_filter = ('title', 'location', 'date',)
    prepopulated_fields = {'slug': ('title',)}


class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('email',)


admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Location)
admin.site.register(Participant, ParticipantAdmin)
