from django.db import models
from users.models import User


class Article(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    likes = models.ManyToManyField(User, related_name="like_articles",blank=True)

    def __str__(self):
        return str(self.title)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete =models.CASCADE)
    article= models.ForeignKey(Article, on_delete =models.CASCADE, related_name = "comment_set")
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)