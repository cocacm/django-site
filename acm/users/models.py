from django.contrib.auth.models import AbstractUser
from django.db import models


class ACMUser(AbstractUser):
    bio = models.TextField(blank=True)
    sid = models.TextField(blank=False, max_length=7)

    class Meta(object):
        unique_together = ('email', 'id', )

    pass
