# Generated by Django 4.2.7 on 2023-11-28 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0002_problem_input_format_problem_output_format'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='example',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]