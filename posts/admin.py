from django.contrib import admin

# Register your models here.
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "timestamp", "updated"]
    list_filter = ["updated"]
    search_field = ["title", "content"]
    class Meta:
        model = Post

admin.site.register(Post, PostModelAdmin)
