from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from .models import Star, Event, ScoreName, EventStarList, StarScores, StarType, Evaluation, YourUser


class StarAdmin(admin.ModelAdmin):
    filter_horizontal = ('events',)
    list_display = ['id', 'name', 'image', 'description', 'type']
    list_filter = ('name',)
    search_fields = ['name']


class ScoreNameAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'score_name']
    list_filter = ('type',)
    search_fields = ['type']


class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'title', 'image', 'description']
    list_filter = ('title',)
    search_fields = ['title']


class EventStarListAdmin(admin.ModelAdmin):
    list_display = ['id', 'event', 'star']
    list_filter = ('event_id',)
    search_fields = ['event_id']


class StarScoresAdmin(admin.ModelAdmin):
    list_display = ['id', 'score', 'score_name', 'star', 'user']
    list_filter = ('score_name',)
    search_fields = ['score_name']


class StarTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'type']
    list_filter = ('type',)
    search_fields = ['type']


class YourUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'image']
    list_filter = ('id',)
    search_fields = ['username']


# class YourUserInline(admin.StackedInline):
#     model = YourUser
#     can_delete = False
#     verbose_name_plural = 'youruser'
#
#
# class UserAdmin(BaseUserAdmin):
#     inlines = (YourUserInline,)


class EvaluationAdmin(admin.ModelAdmin):
    list_display = ['id', 'star_score', 'star', 'feed', 'user']
    list_filter = ('star',)
    search_fields = ['star']


admin.site.register(Star, StarAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(EventStarList, EventStarListAdmin)
admin.site.register(ScoreName, ScoreNameAdmin)
admin.site.register(StarScores, StarScoresAdmin)
admin.site.register(StarType, StarTypeAdmin)
admin.site.register(Evaluation, EvaluationAdmin)
# admin.site.unregister(User)
admin.site.register(YourUser, YourUserAdmin)


