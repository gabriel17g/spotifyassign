from django.contrib import admin
from .models import Artist, Songs

# Register your models here.

class Artistadmin(admin.ModelAdmin):
    list_display = ["name"]
    list_filter = ["name"]
    search_fields = ["name"]

admin.site.register(Artist, Artistadmin)




class Songadmin(admin.ModelAdmin):
    list_display = ["name", "artist", "genre"]
    list_filter = ["name", "artist", "genre"]
    search_fields = ["name", "artist", "genre"]


admin.site.register(Songs, Songadmin)