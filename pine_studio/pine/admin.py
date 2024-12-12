from django.contrib import admin
from .models import creative, pack, download_email, contact

admin.site.register(creative.Creative)
admin.site.register(contact.ContactMessage)
admin.site.register(pack.Pack)
admin.site.register(pack.PackItem)
admin.site.register(download_email.DownloadEmail)
