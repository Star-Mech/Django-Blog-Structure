from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id)))
        return reverse('home')


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(max_length=750)
    profile_pic = models.ImageField(null=True, blank=True, upload_to='profile_img/')
    website_url = models.CharField(max_length=255, null=True, blank=True, default='#')
    twitter_url = models.CharField(max_length=255, null=True, blank=True, default='#')
    linkedin_url = models.CharField(max_length=255, null=True, blank=True, default='#')

    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return str(self.user)



# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    header_img = models.ImageField(null=True, blank=True, upload_to='images/')
    title_tag = models.CharField(max_length=255, default="")
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE)  # on_delete here will delete the posts by the user if user deleted
    body = RichTextField(blank=True, null=True)
    # body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=255, default='Uncategorized')
    snippet = models.CharField(max_length=300)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + " | " + str(self.author)

    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id)))
        return reverse('home')


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_body = RichTextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.time} | {self.user} | {self.comment_body}'