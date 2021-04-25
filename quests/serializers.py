from .models import Quest, Strength, Endurance, Wisdom, User
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class QuestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quest
        fields = ['id', 'name', 'stat', 'total']

class StrengthSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Strength
        fields = ['id', 'name', 'strength']

class EnduranceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Endurance
        fields = ['id', 'name', 'endurance']

class WisdomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Wisdom
        fields = ['id', 'name', 'wisdom']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']