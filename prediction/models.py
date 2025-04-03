from django.db import models

class db(models.Model):
    historical_yield = models.FloatField(null=True)
    rainfall = models.FloatField(null=True)
    humidity = models.FloatField(null=True)
    soil_ph = models.FloatField(null=True)
    organic_content = models.FloatField(null=True)
    predicted_yield = models.FloatField(null=True, blank=True)  
    def __str__(self):
        return f"{self.historical_yield} {self.rainfall} {self.humidity} {self.soil_ph} {self.organic_content}"
