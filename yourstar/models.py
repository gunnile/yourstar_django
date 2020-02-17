from django.db import models


class Event(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    image = models.ImageField(blank=True)
    description = models.TextField()

    class Meta:
        ordering = ('id',)

    def save(self, *args, **kwargs):
        super(Event, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class StarType(models.Model):
    type = models.CharField(max_length=100, blank=True, default='')

    def save(self, *args, **kwargs):
        super(StarType, self).save(*args, **kwargs)

    def __str__(self):
        return self.type


class Star(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    image = models.ImageField(blank=True)
    description = models.TextField()
    type = models.ForeignKey(StarType, blank=True, on_delete=models.CASCADE)
    events = models.ManyToManyField(Event, related_name='star_list', blank=True)

    class Meta:
        ordering = ('id',)

    def save(self, *args, **kwargs):
        super(Star, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class ScoreName(models.Model):
    type = models.ForeignKey(StarType, blank=True, on_delete=models.CASCADE)
    score_name = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ('id',)

    def save(self, *args, **kwargs):
        super(ScoreName, self).save(*args, **kwargs)

    def __str__(self):
        return self.score_name


class StarScores(models.Model):
    score = models.IntegerField(blank=True, default='0')
    score_name = models.ForeignKey(ScoreName, default=True, on_delete=models.CASCADE)
    star = models.ForeignKey(Star, related_name='score_list', default=True, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(StarScores, self).save(*args, **kwargs)

    def __str__(self):
        return self.score_name.score_name


class EventStarList(models.Model):
    event = models.ForeignKey(Event, related_name='tracks', on_delete=models.CASCADE)
    star = models.ForeignKey(Star, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(EventStarList, self).save(*args, **kwargs)


class Evaluation(models.Model):
    # overall = models.IntegerField(blank=True, default='0')
    star_score = models.ForeignKey(StarScores, default=True, on_delete=models.CASCADE)
    star = models.ForeignKey(Star, related_name='evaluation_score_list', on_delete=models.CASCADE)
    feed = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        super(Evaluation, self).save(*args, **kwargs)

    def __str__(self):
        return self.star


# class User(models.Model):
#     username = models.CharField(max_length=100, blank=True, default='')
#     email = models.CharField(max_length=100, blank=True, default='')
#     image = models.ImageField(blank=True)
#     description = models.TextField()
#     stars = models.ForeignKey(Star, related_name='star_list', blank=True, null=True, on_delete=models.CASCADE)
#
#     class Meta:
#         ordering = ('id',)
#
#     def save(self, *args, **kwargs):
#         super(User, self).save(*args, **kwargs)
#
#     def __str__(self):
#         return self.username
