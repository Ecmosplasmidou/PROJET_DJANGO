from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _

class Band(models.Model):
    
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
        RAP = 'RP'
    
    name = models.fields.CharField(max_length=100, verbose_name=_("Nom"))
    genre = models.fields.CharField(choices=Genre.choices, max_length=5, verbose_name=_("Genre"))
    biography = models.fields.CharField(max_length=1000, verbose_name=_("Biographie"))
    year_formed = models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2024)], verbose_name=_("Année de formation"))
    active = models.fields.BooleanField(default=True, verbose_name=_("Actif"))
    official_homepage = models.fields.URLField(null=True, blank=True, verbose_name=_("Site officiel"))
    
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
