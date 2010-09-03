from django.db import models

#import tagging

class Location(models.Model):
    """
    A location at which groceries might be procured.
    """
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class LocationSection(models.Model):
    """
    A section of a location holding specific types of items.
    """
    name = models.CharField(max_length=50)
    location = models.ForeignKey(Location)

    def __unicode__(self):
        return self.name

class GroceryItem(models.Model):
    """
    An item in a grocery list or in the current stock.
    """
    name = models.CharField(max_length=100)
    is_low = models.BooleanField()
    is_out = models.BooleanField()
    stock_date = models.DateTimeField()
    votes = models.IntegerField(default=0)
    locations = models.ManyToManyField(Location)
    one_shot = models.BooleanField()
    
    def __unicode__(self):
        return self.name

#tagging.register(LocationSection)
#tagging.register(GroceryItem)
