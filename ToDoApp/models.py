from django.db import models
from django.utils import timezone
import datetime

# Create your models here.


# here i create the model, it's how your code will looks like
class Todo(models.Model):
    text = models.CharField(max_length=200)
    added_date = models.DateField()

    # i used this just for applying the tests or in other word, to know why we should use test

    def was_recently_published(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.added_date <= now
