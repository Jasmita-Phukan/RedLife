from django.contrib import admin
from .models import details
from .models import EmailIds
from .models import contactinfo

admin.site.register(details)
admin.site.register(EmailIds)
admin.site.register(contactinfo)
