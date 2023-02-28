from rest_framework import serializers

from .models import Project


class ProjectListSerializer(serializers.ModelSerializer):
    direction = serializers.CharField(source='direction.title')

    class Meta:
        model = Project
        fields = ('title', 'get_absolute_url', 'direction', )
