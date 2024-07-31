from django.db import models

# Create your models here.
class FeedBack(models.Model):
    email = models.EmailField(max_length=255, null=True, blank=True)
    message = models.CharField(max_length=100000, null=True)

    def __str__(self):
        return f'{self.email} - {self.message}'