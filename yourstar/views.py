from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, generics
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum

from yourstar.models import Star, Event, ScoreName, EventStarList, StarScores, StarType, Evaluation
from yourstar.permissions import IsAuthenticatedOrCreate
from yourstar.serializers import ScoreNameSerializer, EventStarSerializer, StarScoresSerializer, \
    EventDetailSerializer, StarDetailSerializer, UserSerializer, SignUpSerializer, TypeSerializer, EvaluationSerializer, \
    StarScoresIdSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        event = self.get_object()
        return Response(event.highlighted)


class StarViewSet(viewsets.ModelViewSet):
    queryset = Star.objects.all()
    serializer_class = StarDetailSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        star = self.get_object()
        return Response(star.highlighted)


class ScoreNameViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ScoreName.objects.all()
    serializer_class = ScoreNameSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['type']


class EvaluationViewSet(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer

    # filter_backends = [DjangoFilterBackend]
    # filter_fields = ['star']

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        evaluation = self.get_object()
        return Response(evaluation.highlighted)


class StarScoresViewSet(viewsets.ModelViewSet):
    queryset = StarScores.objects.all()
    serializer_class = StarScoresSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['star']

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        star = self.get_object()
        return Response(star.highlighted)

    # def get(self, request):
    #     """List Transactions"""
    #     starscore = StarScores.objects.all()
    #     serializer = StarScoresSerializer(starscore, many=True)
    #     return_data = {"sum": str(sum([lambda items: int(items['score'])])), "objects": serializer.data}
    #     return Response(return_data)


class StarScoresIdViewSet(viewsets.ModelViewSet):
    queryset = StarScores.objects.all()
    serializer_class = StarScoresIdSerializer


class EventStarListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EventStarList.objects.all()
    serializer_class = EventStarSerializer


class TypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = StarType.objects.all()
    serializer_class = TypeSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SignUp(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    # permission_classes = (IsAuthenticatedOrCreate,)
