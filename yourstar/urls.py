from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.urls import path, include
from rest_framework import serializers
from rest_framework.routers import DefaultRouter
from yourstar import views

from rest_framework import generics, permissions, serializers

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope


# first we define the serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', "first_name", "last_name")


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("name", )


# Create the API views
class UserList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetails(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# Setup the URLs and include login URLs for the browsable API.
urlpatterns = [
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('users/', UserList.as_view()),
    path('users/<pk>/', UserDetails.as_view()),
    path('groups/', GroupList.as_view()),
    url(r'^sign_up/', views.SignUp.as_view(), name="sign_up"),

    # ...
]

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'events', views.EventViewSet)
router.register(r'stars', views.StarViewSet)
router.register(r'event_star_list', views.EventStarListViewSet)
router.register(r'star_scores_list', views.StarScoresViewSet)
router.register(r'scores', views.ScoreNameViewSet)




# The API URLs are now determined automatically by the router.
urlpatterns += [
    path('', include(router.urls)),
    path('accounts/', include('django.contrib.auth.urls')),
]