from django.db import models
from ..models._base import BaseModel
from ..models.pack import Pack


class DownloadEmail(BaseModel):
    found_us_through_choices = [
        ('google', 'Google'),
        ('social_media', 'Mídias Sociais'),
        ('friend', 'Indicação de Amigo'),
        ('other', 'Outro'),
    ]

    name = models.CharField(max_length=255, verbose_name="Nome completo")
    email = models.EmailField(verbose_name="E-mail")
    found_us_through = models.CharField(
        max_length=100,
        choices=found_us_through_choices,
        verbose_name="Por onde nos encontrou?"
    )
    pack = models.ForeignKey(Pack, on_delete=models.SET_NULL, null=True, blank=True, related_name='downloads')
    registered_at = models.DateTimeField(auto_now_add=True)
    consent_for_marketing = models.BooleanField(default=False, verbose_name="Consentimento para marketing")

    def __str__(self):
        return f"{self.name} ({self.email})"
