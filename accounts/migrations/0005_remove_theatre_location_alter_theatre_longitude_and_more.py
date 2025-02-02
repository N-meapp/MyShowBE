# Generated by Django 5.1.4 on 2024-12-16 10:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_theatre_latitude_theatre_longitude'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theatre',
            name='location',
        ),
        migrations.AlterField(
            model_name='theatre',
            name='longitude',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.userlocation'),
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Description', models.TextField()),
                ('Duration', models.CharField(max_length=50)),
                ('language', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=50)),
                ('release_date', models.CharField(max_length=50)),
                ('Theatre_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Theatre_name', to='accounts.theatre')),
            ],
        ),
    ]
