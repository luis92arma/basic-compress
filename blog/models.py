from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    user = models.ForeignKey(User)
    create_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=70)
    content = models.TextField()
    published = models.BooleanField(default=False)
    publication_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.user.username
