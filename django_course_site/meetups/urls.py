from django.urls import path

from . import views

urlpatterns = [
    path('meetups/', views.index, name='all-meetups'),  # our-domain.com/meetups
    path('meetup/<slug:meetup_slug>', views.meetup_detail, name='meetup-detail'),  # our-domain.com/meetup/<dynamic-path-segment>

    path('meetups/myfirstjson', views.my_first_json)  # our-domain.com/meetups/myfirstjson
]
