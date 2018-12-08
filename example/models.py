from django.db import models
from django_mysql.models import JSONField


class Variables(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=150, db_index=True)
    data = JSONField(default=dict)

    def __str__(self):
        return self.name

