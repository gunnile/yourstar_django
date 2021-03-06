# Generated by Django 2.2.1 on 2019-08-17 01:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yourstar', '0005_auto_20190815_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='starscores',
            name='star',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='score_list', to='yourstar.Star'),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, default='', max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('description', models.TextField()),
                ('stars', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='star_list', to='yourstar.Star')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]
