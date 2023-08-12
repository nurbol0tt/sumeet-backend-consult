from django.contrib import admin

from apps.user.models import User, Consultant

# Register your models here.
# admin.site.register(User)
# admin.site.register(Consultant)

# @admin.register(MileStone)
# class MileStoneAdmin(admin.ModelAdmin):
#     list_display = (
#         'id', 'title', 'date_start', 'date_end'
#     )
#     list_display_links = ('id', 'title')
#     search_fields = ('title', 'description', 'task')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
     list_display = (
         'id', 'username', 'phone', 'first_name', 'last_name'
     )


@admin.register(Consultant)
class ConsultantAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'telegram_id',
        'user'
    )
