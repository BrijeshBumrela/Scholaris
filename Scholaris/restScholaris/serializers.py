from rest_framework import serializers
from Discussion_Forum.models import Post
from django.contrib.auth.models import User
from rest_framework.response import Response

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
        )

    def create(self, validated_data):
        return User.objects.create(**validated_data)


    def update(self, instance, validated_data):

        instance.username = validated_data.get('username',instance.username)
        instance.password = validated_data.get('password',instance.password)

        instance.save()
        return instance


class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(max_length=200)

    class Meta:
        model = Post
        fields = (
            'title',
            'body',
            'tag',
            'status',
            'author',
        )


    def update(self, instance, validated_data):

        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.tag = validated_data.get('tag', instance.tag)

        instance.save()

        return instance


class ResultSerializer(serializers.Serializer):
    student = serializers.CharField(max_length=200)
    marks = serializers.IntegerField()


