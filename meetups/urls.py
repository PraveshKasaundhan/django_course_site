from django.urls import path

from . import views

urlpatterns = [
    path("",views.index,name='all-meetups'),
    path("<slug:meet_slug>/success",views.confirm_register,name='confirm-registration'),
    path("<slug:meet_slug>",views.meetup_details,name='meetup-details')

]
