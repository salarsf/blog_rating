from rest_framework import serializers
from .models import (
    Post,
    Rate,
)


class PostSerializer(serializers.ModelSerializer):
    user_rate = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'

    def get_user_rate(self, obj):
        user = self.context['request'].user
        try:
            rate = Rate.objects.get(post=obj, user=user)
            return rate.rating
        except Rate.DoesNotExist:
            return None
