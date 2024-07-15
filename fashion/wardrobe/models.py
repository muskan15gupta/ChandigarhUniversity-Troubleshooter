# wardrobe/models.py
from django.db import models

class WardrobeItem(models.Model):
    CLOTHING_TYPES = [
        ('shirt', 'Shirt'),
        ('pants', 'Pants'),
        ('jacket', 'Jacket'),
        ('dress', 'Dress'),
        # Add other clothing types as needed
    ]
    material = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    image = models.ImageField(upload_to='wardrobe_images/', blank=True)
    

    def __str__(self):
        return self.name

    
