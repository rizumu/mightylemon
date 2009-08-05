from django.db import models
from datetime import date

class Event(models.Model):
    """
    Represents an event you're attending.
    """
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    description = models.TextField()
    location = models.CharField(max_length=150)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(blank=True, null=True)
    link_to_url = models.URLField(max_length=250, blank=True, null=True)

    class Meta:
        ordering = ["-start_date"]
       
    def is_old(self):
        if self.start_date < date.today():
            return True
        return False
    
    def __unicode__(self):
        return "%s on %s" % (self.name, self.when)
    
    
