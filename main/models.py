from django.db import models
from django.utils.text import slugify

from accounts.models import Account
# Create your models here.

"""Messaging"""
class Chat(models.Model):
    participants = models.ManyToManyField(Account, related_name='chats')
    created_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"Chat {self.id}"
    

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Message from {self.sender.user.username} in Chat {self.chat.id}"
    

"""Posts"""
class Post(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug or self.title_has_changed():
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def title_has_changed(self):
        if not self.pk:
            return False
        return Post.objects.filter(pk=self.pk).values_list('title', flat=True).first()
    


    


    
