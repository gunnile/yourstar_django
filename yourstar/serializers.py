from django.contrib.auth import get_user_model
from django.core.files import temp
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count, Sum
from rest_framework import serializers
from rest_framework.utils import json

from yourstar.models import *
import math


class StarSerializer(serializers.ModelSerializer):
    type = serializers.StringRelatedField()

    class Meta:
        model = Star
        fields = ('id', 'name', 'type',  'image',  'description')


class ScoreNameSerializer(serializers.ModelSerializer):
    # type = serializers.StringRelatedField()

    class Meta:
        model = ScoreName
        fields = ('id', 'type', 'score_name')


class StarScoresSerializer(serializers.ModelSerializer):
    score_name = ScoreNameSerializer(many=False, read_only=True)

    class Meta:
        model = StarScores
        fields = '__all__'


class EvalScoreSerializer(serializers.ModelSerializer):
    score_list = serializers.SerializerMethodField()
    overall = serializers.SerializerMethodField()

    def get_score_list(self, obj):
        total_scores = []
        score_elements = ScoreName.objects.filter(type=obj.star.type_id)

        for element in score_elements:
            score_sum = StarScores.objects.filter(id=element.id).aggregate(total_score=Sum('score'))
            score_count = StarScores.objects.filter(score_name__id=element.id).aggregate(total_count=Count('score'))
            test = StarScores.objects.filter(star__id=obj.star.id).aggregate(total_count=Sum('score'))
            print(test)

            total_scores.append({
                "score": 90,
                "element": element.score_name,
                "element_id": element.id
            })

        return total_scores

    def get_overall(self, obj):
        score_sum = StarScores.objects.filter(star__id=obj.star.id).aggregate(total_score=Sum('score'))
        score_count = StarScores.objects.filter(star__id=obj.star.id).aggregate(total_count=Count('score'))

        if score_sum['total_score'] != None:
            overall = round(score_sum['total_score'] / score_count['total_count'])
        else:
            overall = 0

        return overall

    class Meta:
        model = StarScores
        fields = '__all__'


class EvaluationSerializer(serializers.ModelSerializer):
    star_score = EvalScoreSerializer(many=False, read_only=True)

    total_score = serializers.SerializerMethodField()
    total_count = serializers.SerializerMethodField()
    star = StarSerializer(many=False, read_only=True)

    class Meta:
        model = Evaluation
        fields = ('id', 'total_score', 'total_count', 'star_score', 'star', 'feed', 'user')

    def get_total_score(self, obj):
        total_score = StarScores.objects.all().aggregate(total_score=Sum('score'))
        return total_score["total_score"]

    def get_total_count(self, obj):
        total_count = StarScores.objects.all().aggregate(total_count=Count('score'))
        return total_count["total_count"]


class StarScoresIdSerializer(serializers.ModelSerializer):

    class Meta:
        model = StarScores
        fields = ('id', 'score', 'score_name', 'star')


class EventStarSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventStarList
        fields = ('id', 'event', 'star')


class TypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = StarType
        fields = ('id', 'type')


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('id', 'date', 'title', 'image', 'description')


class EventDetailSerializer(serializers.ModelSerializer):
    star_list = StarSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ('id', 'date', 'title', 'image', 'description', 'star_list')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        User = get_user_model()
        model = User
        fields = ('id', 'username')


class YourUserSerializer(serializers.ModelSerializer):
    user_star_score = serializers.SerializerMethodField()
    # user = UserSerializer(many=False, read_only=True)

    def get_user_star_score(self, obj):
        # total_scores = []

        user_star_scores = Evaluation.objects.filter(user__id=obj.id)[:3]
        # user_star_scores = User.objects.filter(id=obj.id)[:3]
        # total_scores.append(user_star_scores)
        serial = EvaluationSerializer(user_star_scores, many=True)
        return serial.data

    class Meta:
        model = YourUser
        # fields = '__all__'
        fields = ('id', 'username', 'image', 'description', 'user_star_score')


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = YourUser
        fields = ('username', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = YourUser(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class StarEvalSerializer(serializers.ModelSerializer):
    # score_name = ScoreNameSerializer(many=False, read_only=True)
    score_list = serializers.SerializerMethodField()
    overall = serializers.SerializerMethodField()
    user = UserSerializer(many=False, read_only=True)

    def get_score_list(self, obj):
        total_scores = []
        score_elements = ScoreName.objects.filter(type=obj.instance.type_id)

        for element in score_elements:
            score_sum = StarScores.objects.filter(score_name__id=element.id).aggregate(total_score=Sum('score'))
            score_count = StarScores.objects.filter(score_name__id=element.id).aggregate(total_count=Count('score'))
            test = StarScores.objects.filter(star__id=obj.instance.id).aggregate(total_count=Sum('score'))
            print(test)

            total_scores.append({
                "average": round(score_sum['total_score'] / score_count['total_count']),
                "total_score": score_sum['total_score'],
                "total_count": score_count['total_count'],
                "element": element.score_name,
                "id": element.id
            })

        return total_scores

    def get_overall(self, obj):
        score_sum = StarScores.objects.filter(star__id=obj.instance.id).aggregate(total_score=Sum('score'))
        score_count = StarScores.objects.filter(star__id=obj.instance.id).aggregate(total_count=Count('score'))

        if score_sum['total_score'] != None:
            overall = round(score_sum['total_score'] / score_count['total_count'])
        else:
            overall = 0

        return overall

    class Meta:
        model = StarScores
        fields = '__all__'


class StarDetailSerializer(serializers.ModelSerializer):

    events = EventSerializer(many=True, read_only=True)
    score_list = StarEvalSerializer(many=False, read_only=True)
    star_eval = serializers.SerializerMethodField()

    def get_star_eval(self, obj):
        star_evals = Evaluation.objects.filter(star__id=obj.id)[:3]
        serial = EvaluationSerializer(star_evals, many=True)
        return serial.data

    class Meta:
        model = Star
        fields = ('id', 'name', 'image', 'description', 'type', 'events', 'score_list', 'star_eval')