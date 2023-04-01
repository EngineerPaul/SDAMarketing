from rest_framework import serializers

from .models import Project


class ProjectListSerializer(serializers.ModelSerializer):
    """ Serializer for listing projects """

    direction = serializers.CharField(source='direction.title')

    class Meta:
        model = Project
        fields = ('title', 'get_absolute_url', 'direction', )


class FeedbackFormSerializer(serializers.Serializer):
    """ Serializer for sending message to email """

    name = serializers.CharField()
    contact = serializers.CharField()
    text = serializers.CharField()
    link = serializers.CharField()
