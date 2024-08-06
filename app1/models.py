from django.db import models
from django.utils import timezone

# Create your models here.
class Code(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,default='UNKNOWN')
    code = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self) -> str:
        return self.name