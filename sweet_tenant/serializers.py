from rest_framework import serializers
from .models import Sweet


class SweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sweet
        fields = ("id", "name")
