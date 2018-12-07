from rest_framework import serializers
from Discussion_Forum.models import Post

class PostSerializer(serializers.Serializer):
    class Meta:
        model = Post
        fields = {
            'title',
            'body',
            'tag',
            'status'
        }