# Generated by Django 2.2.1 on 2019-08-17 01:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yourstar', '0009_auto_20190817_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='stars',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='star_list', to='yourstar.Star'),
        ),
    ]