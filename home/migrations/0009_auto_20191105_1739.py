# Generated by Django 2.1 on 2019-11-05 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_student_roll'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='roll',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]