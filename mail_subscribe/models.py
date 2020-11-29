from django.db import models
from django.utils import timezone

# Create your models here.
from common.models import BaseModel


class MailingList(BaseModel):
    username = models.CharField(max_length=255)
    user_email = models.EmailField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(MailingList, self).save(*args, **kwargs)