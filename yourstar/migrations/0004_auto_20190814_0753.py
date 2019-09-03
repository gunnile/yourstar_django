# Generated by Django 2.2.1 on 2019-08-14 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yourstar', '0003_auto_20190726_0946'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='star',
            options={'ordering': ('id',)},
        ),
        migrations.AddField(
            model_name='star',
            name='events',
            field=models.ManyToManyField(to='yourstar.Event'),
        ),
        migrations.AlterField(
            model_name='eventstarlist',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='yourstar.Event'),
        ),
    ]
