from django.db import models


# Create your models here.

# Creating Company model

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100,
                            choices=(('IT', 'IT'), ('NOn IT', 'Non IT'), ('Mobile Phones', 'Mobiles Phone')))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

# Employee Models
