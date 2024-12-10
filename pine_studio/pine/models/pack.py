from django.db import models
from django.utils.text import slugify
from PIL import Image
from ..models._base import BaseModel
from ..models.tag import Tag


class Pack(BaseModel):
    cover = models.ImageField(upload_to='packs_covers/')
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    is_free = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name='packs', blank=True)
    sales_link = models.URLField(blank=True, null=True)
    items = models.ManyToManyField('PackItem', related_name='packs', blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            truncated_name = self.name[:50]
            base_slug = slugify(truncated_name)
            slug = base_slug
            num = 1

            while Pack.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{num}"
                num += 1
            self.slug = slug[:50]

        super().save(*args, **kwargs)

        if self.cover:
            img = Image.open(self.cover.path)
            if img.height > 1200 or img.width > 1200:
                output_size = (1200, 1200)
                img.thumbnail(output_size)
                img.save(self.cover.path)


class PackItem(BaseModel):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name