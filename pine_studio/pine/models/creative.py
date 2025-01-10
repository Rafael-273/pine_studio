from django.db import models
from ..models._base import BaseModel
from ..models.pack import Pack


class Carousel(BaseModel):
    image = models.ImageField(upload_to='creatives/carousel')

    def __str__(self):
        return self.image

class Creative(BaseModel):
    DIMENSIONS_CHOICES = [
        ('1080x1350', '1080 x 1350'),
        ('1080X1920', '1080 x 1920'),
        ('1080x1080', '1080 x 1080'),
    ]

    pack = models.ForeignKey(Pack, on_delete=models.CASCADE, related_name='creatives')
    is_featured = models.BooleanField(default=False)
    dimensions = models.CharField(
        max_length=9,
        choices=DIMENSIONS_CHOICES,
        default='1080x1350',
    )
    image = models.ImageField(upload_to='creatives/')
    carousels = models.ManyToManyField(Carousel, related_name='creatives', blank=True)

    def __str__(self):
        return self.pack