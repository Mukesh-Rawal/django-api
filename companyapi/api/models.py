from django.db import models

# Create your models here.
# Creating company model

class Company(models.Model):
    comp_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    about = models.TextField()
    types = models.CharField(max_length=100, choices=(('IT', 'IT'), ('Non IT', 'Non IT'), ('Mobiles', 'Mobiles')))

    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# Employee model

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    about = models.TextField()

    position = models.CharField(max_length=50, choices=(
        ('manager', 'manager'),
        ('Software Developer', 'sd'),
        ('Project leader', 'pl'),
    ))

    #company = models.ForeignKey(model, on_delete)

    company = models.ForeignKey(Company, on_delete=models.CASCADE)