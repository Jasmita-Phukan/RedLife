from django.db import models


BLOOD_GROUP_CHOICES = [
    ('A Positive', 'A Positive'),
    ('A Negative', 'A Negative'),
    ('O Positive', 'O Positive')
]

COUNTRY_CHOICES = [
    ('India', 'India')
]
STATE_CHOICES = [
    ('Assam', 'Assam')
]
CITY_CHOICES = [
    ('Guwahati', 'Guwahati')
]
DISTRICT_CHOICES = [
    ('Kamrup', 'Kamrup')
]

class details(models.Model):
    blood_group = models.CharField(
        max_length=100,
        choices=BLOOD_GROUP_CHOICES,
        default='A Positive'
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    country = models.CharField(
        max_length=100,
        choices=COUNTRY_CHOICES,
        default='India'
    )
    state = models.CharField(
        max_length=100,
        choices=STATE_CHOICES,
        default='Assam'
    )
    city = models.CharField(
        max_length=100,
        choices=CITY_CHOICES,
        default='Guwahati'
    )
    district = models.CharField(
        max_length=100,
        choices=DISTRICT_CHOICES,
        default='Kamrup'
    )

    def __str__(self):
        return self.first_name

class EmailIds(models.Model):
    Email = models.EmailField()

    def __str__(self):
        return self.Email
class contactinfo(models.Model):
    First_name= models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    Email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.First_name