# Generated by Django 2.2.1 on 2019-07-26 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ('date',),
            },
        ),
        migrations.CreateModel(
            name='ScoreName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_name', models.CharField(blank=True, default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Star',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='StarScores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(blank=True, default='0')),
                ('score_name', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='yourstar.ScoreName')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yourstar.Star')),
            ],
        ),
        migrations.CreateModel(
            name='EventStarList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yourstar.Event')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yourstar.Star')),
            ],
        ),
    ]
