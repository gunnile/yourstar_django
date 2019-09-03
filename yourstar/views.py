from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, generics
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from yourstar.models import Star, Event, ScoreName, EventStarList, StarScores
from yourstar.permissions import IsAuthenticatedOrCreate
from yourstar.serializers import ScoreNameSerializer, EventStarSerializer, StarScoresSerializer, \
    EventDetailSerializer, StarDetailSerializer, UserSerializer, SignUpSerializer


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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        star = self.get_object()
        return Response(star.highlighted)


class ScoreNameViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ScoreName.objects.all()
    serializer_class = ScoreNameSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['type']


class StarScoresViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = StarScores.objects.all()
    serializer_class = StarScoresSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['star']

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        star = self.get_object()
        return Response(star.highlighted)


class EventStarListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EventStarList.objects.all()
    serializer_class = EventStarSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SignUp(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = (IsAuthenticatedOrCreate,)
