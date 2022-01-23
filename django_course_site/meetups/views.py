from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Meetup
# Create your views here.


# def starting_page():
def index(request):
    # meetups = [
    #     {
    #         'title': 'A First Meetup',
    #         'location': 'New York',
    #         'slug': 'a-first-meetup'
    #     },
    #     {
    #         'title': 'A Second Meetup',
    #         'location': 'Paris',
    #         'slug': 'a-second-meetup'
    #     }
    # ]

    meetups = Meetup.objects.all()

    return render(request, 'meetups/index.html', {
        'show_meetups': True,
        'meetups': meetups
    })


def meetup_detail(request, meetup_slug):
    # selected_meetup = {
    #     'title': 'HARDCODED A First Meetup',
    #     'description': 'HARDCODED This is the first meetup'
    #     # 'location': 'New York',
    #     # 'slug': 'a-first-meetup'
    # }
    try:
        selected_meetup = Meetup.objects.get(slug = meetup_slug)
        return render(request, 'meetups/meetup-detail.html', {
            'meetup_found': True,
            'meetup': selected_meetup

            # 'title': selected_meetup.title,
            # 'description': selected_meetup.description,
            # 'slug': selected_meetup.slug
        })
    except Exception as exc:
        return render(request, 'meetups/meetup-detail.html', {
            'title': '',
            'description': '',
            'meetup_found': False,
        })



def my_first_json(request):
    return JsonResponse({'foo': 'bar'})

