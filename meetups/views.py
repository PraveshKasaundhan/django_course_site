from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Meetup, Participant
from .forms import RegistrationForm
# Create your views here.

def index(request):
    try:
        meetups=Meetup.objects.all()
        return render(request,"meetups/index.html",{'show':True,'meetups':meetups})
    except:
        return render(request,"meetups/index.html",{'show':False,'meetups':meetups})

def meetup_details(request,meet_slug):
    try:
        selected_meet=Meetup.objects.get(slug=meet_slug)
        if request.method=='GET':
            register_form=RegistrationForm()
            return render(request,"meetups/meetup-details.html",{'found':True,'meet':selected_meet,'form':register_form})
        else:
            register_form=RegistrationForm(request.POST)
            if register_form.is_valid():
                useremail=register_form.cleaned_data['email']
                participant, _  = Participant.objects.get_or_create(email=useremail)
                selected_meet.participants.add(participant)
                return redirect("confirm-registration",meet_slug=meet_slug)
        return render(request,"meetups/meetup-details.html",{'found':True,'meet':selected_meet,'form':register_form})
    except:
        return render(request,"meetups/meetup-details.html",{'found':False})

def confirm_register(request,meet_slug):
    selected_meet=Meetup.objects.get(slug=meet_slug)
    return render(request,"meetups/registration-success.html",{'meet':selected_meet})
