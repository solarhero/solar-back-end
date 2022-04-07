from email.policy import default
from inspect import _empty
from lib2to3.pgen2.token import COMMA
from queue import Empty
from django.db import models

COMMENT_TYPE = [
    ('recommend', 'recommend'),
    ('inquiry', 'Sophomore'),
    ('report', 'report'),
    ('complaint', 'complaint'),
    ('other', 'other'),
]


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    type = models.CharField(max_length=255, choices=COMMENT_TYPE)
    comment = models.TextField()


class Feedback(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    feedback = models.JSONField(default=dict)
    other_feedback = models.TextField(blank=True)
