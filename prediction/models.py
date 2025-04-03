from django.db import models

class db(models.Model):
    historical_yield = models.FloatField(null=True)
    rainfall = models.FloatField(null=True)
    humidity = models.FloatField(null=True)
    soil_ph = models.FloatField(null=True)
    organic_content = models.FloatField(null=True)
    predicted_yield = models.FloatField(null=True, blank=True) 

class first(models.Model):
    historical_yield = models.FloatField(null=True)
    rainfall = models.FloatField(null=True)
    humidity = models.FloatField(null=True)
    soil_ph = models.FloatField(null=True)
    organic_content = models.FloatField(null=True)
    predicted_yield = models.FloatField(null=True, blank=True)