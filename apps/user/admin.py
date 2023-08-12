from django.contrib import admin

from apps.user.models import User, Consultant

# Register your models here.
admin.site.register(User)
admin.site.register(Consultant)
