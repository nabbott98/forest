from rest_framework import serializers

from .models.tree import Tree
from .models.park import Park

class TreeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Tree

class ParkSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Park

class ParkViewSerializer(serializers.ModelSerializer):
    tree = serializers.StringRelatedField()
    class Meta:
        fields = '__all__'
        model = Park