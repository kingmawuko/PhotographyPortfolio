from django.db import models


class PolicyModel(models.Model):
    Title = models.CharField(max_length=20, default=None)
    Description = models.TextField(max_length=None,null=True,blank=True)
    def __str__(self):
        return self.Title


class Contact(models.Model):
    Email = models.EmailField()
    Message = models.TextField(max_length=None,null=True,blank=True)
    Subject = models.CharField(max_length=20, default=None)
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
    


# InvoiceModel 

# Traffic Model 

# PriceModel 