from django.db import models


# model for the comments that will persist on blog and event posts
class Comments(models.Model):
    date_time = models.DateTimeField(editable=False, auto_now_add=True)
    content = models.TextField(blank=False)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
