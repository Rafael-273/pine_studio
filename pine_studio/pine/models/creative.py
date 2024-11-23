from django.db import models
from ..models._base import BaseModel
from ..models.pack import Pack


class Creative(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    pack = models.ForeignKey(Pack, on_delete=models.CASCADE, related_name='creatives')
    is_free = models.BooleanField(default=False)
    image = models.ImageField(upload_to='creatives/')

    def __str__(self):
        return self.name
