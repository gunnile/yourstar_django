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

# Setup the URLs and include login URLs for the browsable API.
urlpatterns = [
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^sign_up/', views.SignUp.as_view(), name="sign_up"),
    # url(r'^user/(?P<username>.+)/$', views.UserViewSet),
    # ...
]

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'events', views.EventViewSet)
router.register(r'stars', views.StarViewSet)
router.register(r'event_star_list', views.EventStarListViewSet)
router.register(r'star_scores_list', views.StarScoresViewSet)
router.register(r'users', views.YourUserViewSet)
router.register(r'scores', views.ScoreNameViewSet)
router.register(r'types', views.TypeViewSet)
router.register(r'evaluations', views.EvaluationViewSet)
router.register(r'star_scores_id_list', views.StarScoresIdViewSet)
# router.register(r'signup', views.SignUpViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns += [
    path('', include(router.urls)),
    path('accounts/', include('django.contrib.auth.urls')),
]