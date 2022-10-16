from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Rate


@receiver(post_save, sender=Rate)
def post_rate_receiver(sender, instance, **kwargs):
    post = instance.post
    rates = Rate.objects.filter(post=post).all()

    post.rate_count = rates.count()

    total = 0
    for rate in rates:
        total += rate.rating

    post.rating_average = total / post.rate_count

    post.save()
