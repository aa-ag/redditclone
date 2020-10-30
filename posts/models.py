from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import math

class Post(models.Model):
    title = models.CharField(max_length=200)
    url = models.TextField()
    pub_date = models.DateTimeField()
    votes_total = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def ago(self):
        now = timezone.now()

        time_diff = now - self.pub_date

        if time_diff.days == 0 and time_diff.seconds >= 0 and time_diff.seconds < 60:
            seconds= time_diff.seconds
            
            if seconds == 1:
                return str(seconds) +  "second ago"
            
            else:
                return str(seconds) + " seconds ago"

        if time_diff.days == 0 and time_diff.seconds >= 60 and time_diff.seconds < 3600:
            minutes= math.floor(time_diff.seconds/60)

            if minutes == 1:
                return str(minutes) + " minute ago"
            
            else:
                return str(minutes) + " minutes ago"

        if time_diff.days == 0:
            hours = math.floor(time_diff.seconds/3600)

            if hours <= 1:
                return "posted less than an hour ago"
            else:
                return f"posted {str(hours)} hours ago"
        if time_diff.days >= 1 and time_diff.days < 30:
            d = time_diff.days
            if time_diff.d == 1:
                return "posted yesterday"
            else:
                return f"posted {str(d)} days ago"

        if time_diff.days >= 30 and time_diff.days < 365:
            months = math.floor(time_diff.days/30)

            if months == 1:
                return "posted last month"
            else:
                return f"posted {months} months ago"

        if time_diff.days >= 365:
            years = math.floor(time_diff.days/365)

            if years == 1:
                return "posted last year"
            else:
                return f"posted {years} years ago"