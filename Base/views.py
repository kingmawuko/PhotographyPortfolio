from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import *

# Create your views here.


def WelcomeView(request):
    context = {}
    return render(request,'Base/Welcome.html',context)

def ContactView(request):
    if 'SendForm' in request.POST:   
        message = request.POST.get('message')
        Email = request.POST.get('email')
        Name = request.POST.get('name')    
        contact=Contact.objects.create(Name=Name,Email=Email,Message=message)
        #Message = f' "{contact.Subject}" form submitted from {contact.email}. They mentioned in their message ({contact.Message})'
        print({'Email':Email,'message':message,'Name':Name})
        messages.info(request,'Thank you for your message. You will be contacted soon. Form submission successful') 
        #Subject = f' ! Freelance Service !'
        #email = 'mawukoattivor@gmail.com'
        #send_mail(Subject, Message, email, [email], fail_silently=False)
        # Message.messages

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
    if 'SubmitForm' in request.POST:   
        location = request.POST.get('location')
        phone = request.POST.get('phone')
        email = request.POST.get('email') 
        name= request.POST.get('name') 
        AppointmentRequest.objects.create(Location=location,PhoneNum=phone,Email=email)
        print({'location':location,'phone':phone,'email':email})
        messages.info(request,'Thank you !  You will be contacted soon. Appointment submission successful') 
    context = {}
    return render(request,'Base/Appointment.html',context)

def InvoiceView(request):
    if request.method == 'POST':
         InvoiceNum = request.POST.get('InvoiceNum')
         InvoiceEmail=request.POST.get('email')
         print({'Invoice id':InvoiceNum,'Email':InvoiceEmail})
         invoice = InvoiceModel.objects.filter(Invoice=InvoiceNum,Email=InvoiceEmail).first() 
         if invoice:  
            if invoice.status == 'No':  
                invoice.status = 'No'
                invoice.save()
                return redirect('Base:Review', InvoiceNum=InvoiceNum)        
         if invoice: 
            if invoice.status == 'completed':          
                return redirect('Base:Completed', InvoiceNum=InvoiceNum)  
            if invoice.status == 'partial': 
                    print('redirect to partial')
            return redirect('Base:Partial', InvoiceNum=InvoiceNum)  
         else:  
            messages.info(request, 'Incorrect invoice ID.')
    context = {}
    return render(request,'Base/Invoice.html',context)

def InvoiceReviewView(request,InvoiceNum):
    Invoice = get_object_or_404(InvoiceModel, Invoice=InvoiceNum)  
    if Invoice: 
            if Invoice.status == 'No': 
                Invoice.status = 'No'
                Invoice.save()      
    context = {'Invoice': Invoice}
    return render(request, 'Base/InvoiceReview.html', context)

def InvoicePartialView(request, InvoiceNum):
    Invoice = get_object_or_404(InvoiceModel, Invoice=InvoiceNum)
    if Invoice: 
        # if the invoice status is partial set the EmailStatus to Partial too and save else none 
        if Invoice.status != 'partial':
            Invoice.EmailStatus = 'Partial'
            print({'Invoice status ':Invoice.status})
            print({' EmailStatus':Invoice.EmailStatus})
            Invoice.status = 'partial'
            Invoice.save()
            # if the Emailstatus is partial send both emails 
            if Invoice.EmailStatus == 'Partial':
               # client_message = f'Thanks. Your payment has been processed and I will begin work on your project. If you have any questions, please feel free to ask.'
                #client_subject = f' Payment Received'
                #client_email =Invoice.Email
                #send_mail(client_subject, client_message, client_email, [Invoice.Email], fail_silently=False)
               
                #admin_message = f'A partial payment has been received from {Invoice.Email}.'
                #admin_subject = f'! Portfolio Message ! Partial Payment Received'
                #admin_email = 'mawukoattivor@gmail.com' 
                #send_mail(admin_subject, admin_message, client_email, [admin_email], fail_silently=False)
                Invoice.EmailStatus = 'Partial' 
            else:
                None  
    context = {'Invoice': Invoice}
    return render(request, 'Base/Partial.html', context)

def InvoiceCompleteView(request, InvoiceNum):
    Invoice = get_object_or_404(InvoiceModel, Invoice=InvoiceNum)
    if Invoice: 
        if Invoice.status != 'completed':
            Invoice.status = 'completed'
            Invoice.save()       
            if Invoice.EmailStatus == 'None':    
                client_message = f'Thanks. Your payment has been completed and your project is now finished. If you have any questions or concerns, please feel free to contact me for support, upgrades, or add-ons.'
                client_subject = f'Payment Completed'
               # client_email = Invoice.Email
               # send_mail(client_subject, client_message, client_email, [Invoice.Email], fail_silently=False)          
                #admin_message = f'{Invoice.Email} has completed the payment for their project.'
                #admin_subject = f'! Portfolio Message ! Payment Completed'
                #admin_email = 'mawukoattivor@gmail.com' 
                #send_mail(admin_subject, admin_message, client_email, [admin_email], fail_silently=False)
                Invoice.EmailStatus == 'Partial'
            else:
                None
    context = {'Invoice': Invoice}
    return render(request, 'Base/Completed.html', context)


