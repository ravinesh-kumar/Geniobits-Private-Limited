from django.db import models

# Create your models here.
class MainApp(models.Model):
    BANKNIFTY = models.CharField(("BANKNIFTY"),max_length=255)
    DATE = models.IntegerField(("DATE"))
    TIME = models.IntegerField(("TIME"))
    OPEN = models.FloatField(("OPEN"))
    HIGH = models.FloatField(("HIGH"))
    LOW = models.FloatField(("LOW"))
    CLOSE = models.FloatField(("CLOSE"))
    VOLUME = models.FloatField(("VOLUME"))
    
