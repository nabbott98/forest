from rest_framework import serializers

from .models import Tree

class TreeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Tree