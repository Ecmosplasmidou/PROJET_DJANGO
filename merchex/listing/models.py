from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Band(models.Model):
    
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
        RAP = 'RP'
    
    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2024)])
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class Listing(models.Model):
    
    class Type(models.TextChoices):
        RECORDS = 'RD'
        CLOTHING = 'CL'
        POSTERS = 'PS'
        MISCELLANOUS = 'MS'
    
    title = models.fields.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(validators=[MinValueValidator(1950), MaxValueValidator(2024)], null=True, blank=True)
    type = models.fields.CharField(choices=Type.choices, max_length=5)
    band = models.ForeignKey(Band, null = True, on_delete=models.SET_NULL) #models.cascade sert à supprimer les listings si l'object Band est supprimé
