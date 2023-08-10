import uuid

from django.db import models

from apps.user.models import User, Consultant


class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    consultant = models.ForeignKey(Consultant, on_delete=models.CASCADE)
    TOPIC_CHOICES = (
        (1, 'Topic 1'),
        (2, 'Topic 2'),
    )
    topic = models.IntegerField(choices=TOPIC_CHOICES)
    text = models.TextField()
    result = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


class Answer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    answer = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
