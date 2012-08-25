from django.db import models
from django.contrib.comments.models import Comment

class MarkdownComment(Comment):
    is_markdown = models.BooleanField()