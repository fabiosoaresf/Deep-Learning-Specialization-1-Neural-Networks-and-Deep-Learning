from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.

# def starting_page():
def index(request):
    meetups = [
        {
            'title': 'A First Meetup',
            'location': 'New York',
            'slug': 'a-first-meetup'
        },
        {
            'title': 'A Second Meetup',
            'location': 'Paris',
            'slug': 'a-second-meetup'
        }
    ]
    return render(request, 'meetups/index.html', {
        'show_meetups': True,
        'meetups': meetups
    })


def meetup_detail(request, meetup_slug):
    selected_meetup = {
        'title': 'HARDCODED A First Meetup',
        'description': 'HARDCODED This is the first meetup'
        # 'location': 'New York',
        # 'slug': 'a-first-meetup'
    }

    return render(request, 'meetups/meetup-detail.html', {
        'selected_meetup': selected_meetup
    })


def my_first_json(request):
    return JsonResponse({'foo': 'bar'})

