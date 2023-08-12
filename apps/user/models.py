import uuid

from django.db import models


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=255)
    phone = models.CharField(max_length=25)
    photo = models.ImageField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.username


class Consultant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    telegram_id = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="consultant")

    def __str__(self) -> str:
        return self.user.username
