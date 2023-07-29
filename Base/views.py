from django.shortcuts import render
from .models import *

# Create your views here.


def WelcomeView(request):
    context = {}
    return render(request,'Base/Welcome.html',context)



def ContactView(request):
    context = {}
    return render(request,'Base/Contact.html',context)



def PolicyView(request):
    context = {}
    return render(request,'Base/Policy.html',context)


def QuestionsView(request):
    Faq=CommonQuestion.objects.all()

    # Common Questions 
    context = {'Faq':Faq}
    return render(request,'Base/Questions.html',context)


def PriceView(request):
    context = {}
    return render(request,'Base/Price.html',context)


def AboutView(request):
    context = {}
    return render(request,'Base/About.html',context)


def AppointmentView(request):
    context = {}
    return render(request,'Base/Appointment.html',context)


# INvoice 

