from django.db import models

class PersonDonation(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    email = models.EmailField()
    what_to_donate = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self):
        return self.name
