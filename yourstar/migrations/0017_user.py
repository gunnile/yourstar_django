# Generated by Django 2.2.1 on 2020-02-20 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yourstar', '0016_auto_20200216_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, default='', max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('description', models.TextField()),
                ('stars', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='star_list', to='yourstar.Star')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]
