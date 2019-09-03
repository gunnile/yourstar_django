from django.contrib.auth.models import User
from rest_framework import serializers
from yourstar.models import *


class StarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Star
        fields = ('id', 'name', 'image', 'description', 'type')


class ScoreNameSerializer(serializers.ModelSerializer):
    type = serializers.StringRelatedField()

    class Meta:
        model = ScoreName
        fields = ('id', 'type', 'score_name')


class StarScoresSerializer(serializers.ModelSerializer):
    score_name = serializers.StringRelatedField()

    class Meta:
        model = StarScores
        fields = ('score', 'score_name')


class EventStarSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventStarList
        fields = ('id', 'event', 'star')


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('id', 'date', 'title', 'image', 'description')


class EventDetailSerializer(serializers.ModelSerializer):
    star_list = StarSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ('id', 'date', 'title', 'image', 'description', 'star_list')


class StarDetailSerializer(serializers.ModelSerializer):
    events = EventSerializer(many=True, read_only=True)
    score_list = StarScoresSerializer(many=True, read_only=True)

    class Meta:
        model = Star
        fields = ('id', 'name', 'image', 'description', 'type', 'events', 'score_list')


class UserSerializer(serializers.ModelSerializer):
    star_list = StarSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'stars')


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

