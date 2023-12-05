# Generated by Django 4.2.7 on 2023-12-05 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0007_problem_model_solution'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestCaseGenerator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generator_code', models.FileField(upload_to='generators/')),
                ('number_of_testcases', models.IntegerField(default=10)),
                ('problem', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='judge.problem')),
            ],
        ),
    ]
