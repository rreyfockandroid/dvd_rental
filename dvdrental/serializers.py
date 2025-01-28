from rest_framework import serializers
from .models import *

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'


class FilmSerializer(serializers.ModelSerializer):
    actor = ActorSerializer(many=True, read_only=True)
    language = serializers.StringRelatedField()
    
    class Meta:
        model = Film
        fields = '__all__'


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'