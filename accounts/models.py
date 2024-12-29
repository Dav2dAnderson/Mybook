from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=15)
    
    def __str__(self):
        return self.user.username
    

class Channel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='channel_images/', null=True, blank=True)
    link = models.URLField(max_length=150)
    created_date = models.DateField(auto_now_add=True, null=True, blank=True)    
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug or self.title_has_changed():
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def title_has_changed(self):
        if not self.pk:
            return False
        old_title = Channel.objects.filter(pk=self.pk).values_list('title', flat=True).first()
        return old_title != self.title
    

class Group(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='group_images/', null=True, blank=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)
    link = models.URLField(max_length=150, null=True, blank=True)
    created_date = models.DateField(auto_now_add=True, null=True, blank=True)
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug or self.title_has_changed():
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def title_has_changed(self):
        if not self.pk:
            return False
        old_title = Group.objects.filter(pk=self.pk).values_list('title', flat=True).first()
        return old_title != self.title






