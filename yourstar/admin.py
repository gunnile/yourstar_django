from django.contrib import admin

from .models import Star, Event, ScoreName, EventStarList, StarScores, StarType, Evaluation


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
    list_display = ['id', 'score', 'score_name', 'star']
    list_filter = ('score_name',)
    search_fields = ['score_name']


class StarTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'type']
    list_filter = ('type',)
    search_fields = ['type']


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'stars']
    list_filter = ('username',)
    search_fields = ['username']


class EvaluationAdmin(admin.ModelAdmin):
    list_display = ['id', 'star_score', 'star', 'feed']
    list_filter = ('star',)
    search_fields = ['star']


admin.site.register(Star, StarAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(EventStarList, EventStarListAdmin)
admin.site.register(ScoreName, ScoreNameAdmin)
admin.site.register(StarScores, StarScoresAdmin)
admin.site.register(StarType, StarTypeAdmin)
admin.site.register(Evaluation, EvaluationAdmin)
# admin.site.register(User, UserAdmin)


