from rest_framework import serializers
from .models import Usage
import rest_framework


class UsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usage
        fields = ['timestamp', 'daytime', 'nighttime']

    def create(self, validated_data):
        usage = Usage.objects.create(
            timestamp=validated_data['timestamp'],
            daytime=validated_data['daytime'],
            nighttime=validated_data['nighttime'],
        )
        return usage