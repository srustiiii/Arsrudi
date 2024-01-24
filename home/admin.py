from django.contrib import admin
from home.models import Contact

admin.site.site_header = "Ignyt | Admin"
admin.site.register(Contact)
