from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Post(models.Model):
    serialNo=models.AutoField(primary_key=True)
    title=models.CharField(max_length=500)
    content=models.TextField()
    author=models.CharField(max_length=200)
    slug=models.CharField(max_length=200)
    views=models.IntegerField(default=0)
    timestamp=models.DateTimeField(blank=True)

    def __str__(self):
        return 'Blog '+self.title+' by '+self.author

class BlogComment(models.Model):
    serialNo=models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timestamp=models.DateTimeField(default=now)

    def __str__(self):
        return self.comment+"..."+" by "+self.user.username