from os import name
from django.db import models


class Owner(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Pet(models.Model):

    PET_TYPE_CHOICES = [
        ("dog", "Dog"),
        ("cat", "Cat"),
        ("bird", "Bird"),
        ("rabbit", "Rabbit"),
        ("hamster", "Hamster"),
        ("turtle", "Turtle"),
        ("other", "Other"),
    ]

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.CharField(max_length=100)
    pet_type = models.CharField(max_length=100, choices=PET_TYPE_CHOICES)

    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name="pets")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="appointments")
    date = models.DateField()
    time = models.TimeField()
    reason = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.pet.name} - {self.date} - {self.time}"
