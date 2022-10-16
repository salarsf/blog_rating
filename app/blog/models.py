from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    rating_average = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    rate_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
