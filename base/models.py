from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.IntegerField()
    details = models.TextField()
    image = models.ImageField(upload_to='course/')
    is_active = models.BooleanField(default=True, null=False, blank=True)
