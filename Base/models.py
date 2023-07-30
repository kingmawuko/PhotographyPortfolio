from django.db import models
import decimal
import string
import random


class PolicyModel(models.Model):
    Title = models.CharField(max_length=20, default=None)
    Description = models.TextField(max_length=None,null=True,blank=True)
    def __str__(self):
        return self.Title

class Contact(models.Model):
    Email = models.EmailField()
    Message = models.TextField(max_length=None,null=True,blank=True)
    Name = models.CharField(max_length=20, default=None)
    Date = models.DateField(auto_now_add=True,null=True)
    
    def __str__(self):
        return self.Email
    
class CommonQuestion(models.Model):
    Title= models.CharField(max_length=300,null=True,blank=True)
    Question = models.TextField(null=True,blank=True)  

    def __str__(self):
        return self.Title
    
class ServiceType(models.Model):
    Service= models.CharField(max_length=50, null=True, blank=True)
    Description = models.TextField(max_length=None, null=True, blank=True) 
    BaseFee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=None)

    def __str__(self):
        return f"{self.Service} ${self.BaseFee}"
    

class AppointmentRequest(models.Model): 
    Location = models.CharField(max_length=300,null=True,blank=True)
    PhoneNum  = models.CharField(max_length=300,null=True,blank=True)
    Name = models.CharField(max_length=300,null=True,blank=True)
    Email = models.EmailField()
    Date = models.DateField(auto_now_add=True,null=True,blank=True) 

    def __str__(self):
        return f"{self.Name}"



class AdditionalFeatures(models.Model):
    Feature= models.CharField(max_length=50, null=True, blank=True) 
    Description = models.TextField(max_length=None, null=True, blank=True) 
    Price= models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=None)
    def __str__(self):

        return f"{self.Feature} ${self.Price}"




class InvoiceModel(models.Model):
    SERVICE_CHOICES = [
        ('Photo session', 'Photo session'),
        ('Drone', 'Drone')]
    
    EmailStatus = [
        ('Partial', 'Partial'),
        ('Completed', 'Completed'),
        ('None', 'None'),
    ]

    Service = models.CharField(max_length=50, choices=SERVICE_CHOICES, null=True, blank=True)
    Invoice = models.CharField(max_length=25, null=True, blank=True, unique=True)
    status = models.CharField(max_length=10, choices=(('partial', 'partial'), ('completed', 'completed'), ('No', 'No'), ('Refunded', 'Refunded')), default='No') 
    Basepay = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    additional_features = models.ManyToManyField(AdditionalFeatures, blank=True)
    Email = models.EmailField(default='EmailField')  
    EmailStatus = models.CharField(max_length=10, choices=EmailStatus, default='None')
    Date = models.DateField(auto_now_add=True) 
  
    def Tax(self):
        tax_rate = decimal.Decimal('0.0625')
        tax = decimal.Decimal(self.Basepay) * decimal.Decimal(tax_rate)
        return tax.quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_HALF_UP)

    def TotalDue(self):
        total = self.Basepay + self.Tax()

        for feature in self.additional_features.all():
            total += feature.Price

        return round(decimal.Decimal(total), 2)


    def DownPayment(self):
        return round(self.TotalDue() * decimal.Decimal('0.1'), 2)

    def FullPayment(self):
        return round(self.TotalDue() * decimal.Decimal('0.9'), 2)

    def save(self, *args, **kwargs):
        if not self.Invoice:        
            length = 5
            letters_and_digits = string.ascii_uppercase + string.digits
            invoice_number = ''.join(random.choice(letters_and_digits) for i in range(length))
            self.Invoice = invoice_number
        SERVICE_PRICES = {
            'Photo session': 1,
            'Drone': 150,
        }
        self.Basepay = SERVICE_PRICES.get(self.Service, 0)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.status} - Payment for {self.Service}"