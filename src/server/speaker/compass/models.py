from django.db import models

class CompassPage(models.Model):

    name = models.CharField(max_length=50)
    content = models.TextField(blank=True)

    def __unicode__(self):
        return self.name

