from django.db import models
from ..models._base import BaseModel


class Pack(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    is_free = models.BooleanField(default=False)

    def __str__(self):
        return self.name