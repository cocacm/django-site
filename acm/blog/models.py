from django.db import models


# model for each individual blog post
class Blog(models.Model):
    date_time = models.DateTimeField(editable=False, auto_now_add=True)
    title = models.TextField(blank=False)
    content = models.TextField(blank=False)
    image = models.ImageField(null=True, blank=True)

    comments = models.ForeignKey('comments.Comments', models.DO_NOTHING, null=True, blank=True)
