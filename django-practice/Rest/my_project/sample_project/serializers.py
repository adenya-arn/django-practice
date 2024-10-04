from datetime import datetime
from rest_framework import serializers


class Comment:
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()


class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=100)
    created = serializers.DateTimeField()

    def create(self, validated_data):
        return Comment(
            email=validated_data.get("email"),
            content=validated_data.get("content"),
            created=validated_data.get("created"),
        )
        #or you can do this
        #return(**vaidated_data)

    def update (self, instance, validated_data):
            instance.email=validated_data.get("email"),
            instance.content=validated_data.get("content"),
            instance.created=validated_data.get("created"),
            return instance