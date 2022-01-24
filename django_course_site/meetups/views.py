from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from .models import Meetup, Participant
from .forms import RegistrationForm
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
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        if request.method == 'GET':
            registration_form = RegistrationForm()
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():  # form is valid. Store data into database
                user_email = registration_form.cleaned_data['email']
                participant, was_created = Participant.objects.get_or_create(email=user_email)
                selected_meetup.participants.add(participant)
                return redirect('confirm-registration', meetup_slug=meetup_slug)  # redirect the user to a successfully registered webpage

        return render(request, 'meetups/meetup-detail.html', {
            'meetup_found': True,
            'meetup': selected_meetup,
            'registration_form': registration_form
        })
    except Exception as exc:
        print('Exception happened!', exc)
        return render(request, 'meetups/meetup-detail.html', {
            'title': '',
            'description': '',
            'meetup_found': False,
        })


def my_first_json(request):
    return JsonResponse({'foo': 'bar'})


def confirm_registration(request, meetup_slug):
    print('meetup_slug=', meetup_slug)
    meetup = Meetup.objects.get(slug=meetup_slug)
    return render(request, 'meetups/registration-success.html', {
        'organizer_email': meetup.organizer_email
    })
