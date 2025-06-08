from django.db import models

class Stimme(models.Model):
    fach = models.CharField(max_length=100)
    abgegeben_am = models.DateTimeField(auto_now_add=True)
