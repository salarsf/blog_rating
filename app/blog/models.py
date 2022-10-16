from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import (
    MaxValueValidator,
    MinValueValidator,
)

# Create your models here.
User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    rating_average = models.DecimalField(max_digits=2, decimal_places=1, default=0,
                                         validators=[MaxValueValidator(5), MinValueValidator(0)])
    rate_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class Rate(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='rates')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rates')
    rating = models.PositiveSmallIntegerField(validators=[MaxValueValidator(5), MinValueValidator(0)])

    class Meta:
        unique_together = (
            ('post', 'user'),
        )

    def __str__(self):
        return f"{self.post} - {self.user} - {self.rating}"
