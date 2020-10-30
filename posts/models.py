from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    url = models.TextField()
    pub_date = models.DateTimeField()
    votes_total = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # TO DO: convert pub_date to "X hours ago"