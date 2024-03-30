from django.db import models

# Create your models here.

class Participant(models.Model):
    email=models.EmailField(max_length=50,unique=True)

    def __str__(self) -> str:
        return f"{self.email}"

class Location(models.Model):
    name=models.CharField(max_length=25)
    address=models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name} ({self.address})"

class Meetup(models.Model):
    title=models.CharField(max_length=25)
    description=models.TextField(max_length=50)
    image=models.ImageField(upload_to='images')
    slug=models.SlugField(unique=True)
    organizer=models.EmailField(max_length=50)
    date=models.DateField()

    location=models.ForeignKey(Location, on_delete=models.CASCADE)
    participants=models.ManyToManyField(Participant, blank=True)

    def __str__(self) -> str:
        return f"{self.title} | {self.description} | {self.date}"