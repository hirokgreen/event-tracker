import uuid
from django.db import models

# Defining Event model
class Event(models.Model):
    name = models.TextField(blank=True, null=True)
    alias = models.UUIDField(
        default=uuid.uuid4, editable=False, db_index=True, unique=True)
    url = models.URLField()

    class Meta:
        ordering = ('-pk',)
        verbose_name_plural = "Events"
