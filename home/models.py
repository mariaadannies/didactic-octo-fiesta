from django.db import models
from django.conf import settings

# Create your models here.
class Posts(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    content = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
