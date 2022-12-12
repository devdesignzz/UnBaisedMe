from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from .helpers import *
import django.utils.timezone
from ckeditor.fields import RichTextField

# Create your models here.


class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"
        
    name = models.CharField(max_length=255)
    tagline = models.CharField(max_length=510)
    about = models.TextField()
    thumbnail_image = models.ImageField(upload_to='pics/category/thumbnail')
    banner_image = models.ImageField(upload_to='pcis/category/banner', null=True, blank=True)
    slug = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    
    def save(self, *args, **kwargs):
        self.slug = generate_slug_category(self.name)
        super(Category, self).save(*args, **kwargs)

    
    def get_absolute_url(self):
        return reverse('posts')


class Post(models.Model):
    title = models.CharField(max_length=255)
    question = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateTimeField(default=django.utils.timezone.now)
    likes = models.ManyToManyField(User, related_name='question_posts')
    slug = models.SlugField(max_length=1001, null=True, blank=True)

    def __str__(self):
        return self.title + " | " + str(self.author)

    
    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(Post, self).save(*args, **kwargs)

    
    def get_absolute_url(self):
        return reverse('posts')


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments' ,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return self.post.title + " | " + str(self.name)


class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    review = models.TextField()
    picture = models.ImageField(upload_to='pics/testimonials/')

    def __str__(self):
        return self.name + " | " + str(self.designation)



