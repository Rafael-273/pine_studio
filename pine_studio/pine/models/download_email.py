from django.db import models
from ..models._base import BaseModel
from ..models.pack import Pack


class DownloadEmail(BaseModel):
    email = models.EmailField(unique=True)
    registered_at = models.DateTimeField(auto_now_add=True)
    pack = models.ForeignKey(Pack, on_delete=models.SET_NULL, null=True, blank=True, related_name='downloads')

    def __str__(self):
        return self.email
