# Generated by Django 2.2.1 on 2020-02-20 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yourstar', '0019_starscores_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluation',
            name='user',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='evaluation_user', to='yourstar.User'),
        ),
        migrations.AlterField(
            model_name='starscores',
            name='user',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='score_user', to='yourstar.User'),
        ),
    ]
