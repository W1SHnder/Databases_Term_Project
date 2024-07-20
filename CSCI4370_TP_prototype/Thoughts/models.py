from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Thought(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    public = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'Thought'

class Idea(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'Idea'

class Link(models.Model): 
    idea = models.ForeignKey(Idea, on_delete=models.DO_NOTHING)
    thought_a = models.ForeignKey(Thought, on_delete=models.CASCADE, related_name='%(class)s_thought_a')
    thought_b = models.ForeignKey(Thought, on_delete=models.CASCADE, related_name='%(class)s_thought_b')

    class Link:
        db_table = 'Link'


class Tag(models.Model):
    thought = models.ManyToManyField(Thought)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Tag'
