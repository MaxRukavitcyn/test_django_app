from django.contrib import admin

# Register your models here.
from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_pub', 'date_mod', 'is_published')


admin.site.register(News, NewsAdmin)
