from django.db import models

# Create your models here.

class UserLocation(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s location"

class City(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="city_uploads")

    def __str__ (self):
        return self.name
    
class Theatre(models.Model):
    name = models.CharField( max_length=50)
    address = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()
    city = models.ForeignKey(City,related_name="Theatres", on_delete=models.CASCADE)

    def __str__(self):
        return  self.name
    

    
class Movie(models.Model):
    name = models.CharField(max_length=100)
    Description = models.TextField()
    Duration = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    release_date=models.CharField(max_length=50)
    