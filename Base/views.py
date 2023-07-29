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
    Info=PolicyModel.objects.all()
    context = {'Info':Info}
    return render(request,'Base/Policy.html',context)


def QuestionsView(request):
    Faq=CommonQuestion.objects.all()

    # Common Questions 
    context = {'Faq':Faq}
    return render(request,'Base/Questions.html',context)


def PriceView(request):
    Service=ServiceType.objects.all()
    context = {'Service':Service}
    return render(request,'Base/Price.html',context)


def AboutView(request):
    context = {}
    return render(request,'Base/About.html',context)


def AppointmentView(request):
    context = {}
    return render(request,'Base/Appointment.html',context)



def InvoiceView(request):
    context = {}
    return render(request,'Base/Invoice.html',context)


# INvoice 

