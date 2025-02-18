from django.db import models

class SugarcaneYield(models.Model):
    historical_yield = models.FloatField()
    rainfall = models.FloatField()
    humidity = models.FloatField()
    soil_ph = models.FloatField()
    organic_content = models.FloatField()
    predicted_yield = models.FloatField(null=True, blank=True)  
    timestamp = models.DateTimeField(auto_now_add=True)  # Ensure this field exists

    def __str__(self):
        return f"Yield Prediction ({self.created_at}) - {self.predicted_yield} Tons"
