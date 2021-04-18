from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 
from django.urls import reverse


class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)

    def number_of_likes(self):
        return self.likes.count()
        
    def __str__(self):                          #redirect isnt used, we need to return a string,django already has the redirect built in
        return self.title


    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text

# content=models.TextField()
#     date_posted=models.DateTimeField(default=timezone.now)
#     author=models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):                          #redirect isnt used, we need to return a string,django already has the redirect built in
#         return self.title


#     def get_absolute_url(self):
#         return reverse('post-detail',kwargs={'pk':self.pk})