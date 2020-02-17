# Generated by Django 2.2.1 on 2020-02-16 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yourstar', '0013_auto_20200216_1449'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='starscores',
            name='feed',
        ),
        migrations.RemoveField(
            model_name='starscores',
            name='star',
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('overall', models.IntegerField(blank=True, default='0')),
                ('feed', models.TextField(blank=True)),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='score_list', to='yourstar.Star')),
                ('star_score', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='yourstar.StarScores')),
            ],
        ),
    ]
