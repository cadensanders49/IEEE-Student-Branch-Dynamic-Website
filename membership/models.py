from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    funding = models.FloatField()

class Item(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.IntegerField()

class Member(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    email = models.EmailField()
    phoneNumber = models.IntegerField()
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    YEAR_IN_SCHOOL_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    )
    classification = models.CharField(max_length=200, choices=YEAR_IN_SCHOOL_CHOICES, default=FRESHMAN)
    officerStatus = models.BooleanField()
    officerType = models.CharField(max_length=200)
    duesPaid = models.BooleanField()
    pass
