from rest_framework import serializers

from .models import Post, Account


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        account = Account.objects.get(user=user)
        validated_data['author'] = account
        return super().create(validated_data)


