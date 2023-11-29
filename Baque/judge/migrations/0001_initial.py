# Generated by Django 4.2.7 on 2023-11-28 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('statement', models.TextField()),
                ('timelimit', models.IntegerField(default=1000)),
            ],
        ),
    ]
