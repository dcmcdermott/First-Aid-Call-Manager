from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Responder)
admin.site.register(Call)
admin.site.register(Walkin)
admin.site.register(Minor)
admin.site.register(Schedule)