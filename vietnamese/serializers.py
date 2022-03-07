from rest_framework import serializers

class PyViSerializer(serializers.Serializer):
    text = serializers.CharField()

