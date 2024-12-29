from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Chat, Message, Post
# Register your models here.

admin.site.register(Chat)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('chat', )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at', 'views', 'view_image')
    list_filter = ('title', 'author')

    def view_image(self, post): 
        if post.image:
            return mark_safe(f"<img src='{post.image.url}' width='60' height='60' />")
    view_image.short_description = "Image"
