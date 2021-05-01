from django.contrib.auth.models import User
from django.db.models.expressions import OrderBy
from django.utils import timezone
from django.db import models


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=255)
    slug = models.SlugField(
                max_length=255,
                unique_for_date='publish',
                null=False,
                blank=False,
                unique=True
            )
    author = models.ForeignKey(
                User,
                on_delete=models.CASCADE,
                related_name='blog_posts',
                null=True,
                blank=True
            )
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
                max_length=10, choices=STATUS_CHOICES, default='draft'
            )

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
