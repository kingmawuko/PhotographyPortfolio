
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from .views import *


app_name = 'Base'
urlpatterns = [
    path('', WelcomeView , name='Welcome'),
    path('About/', AboutView , name='About'),
    path('Contact/', ContactView , name='Contact'),
    path('Questions/', QuestionsView , name='Questions'),
    path('Appointment/', AppointmentView , name='Appointment'),
    path('Price/', PriceView , name='Price'),
    path('Invoice/', InvoiceView , name='Invoice'),
    path('Policy/', PolicyView , name='Policy'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)