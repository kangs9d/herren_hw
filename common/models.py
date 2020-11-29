import uuid as uuid
from django.db import models

# Create your models here.
class BaseModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    created_at = models.DateTimeField()
    created_by = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField()
    updated_by = models.IntegerField(null=True, blank=True)

    deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True