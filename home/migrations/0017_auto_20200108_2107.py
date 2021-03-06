# Generated by Django 2.2.6 on 2020-01-08 15:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20200106_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='tmnum',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='branch',
            name='tnum',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='branch',
            name='branchName',
            field=models.CharField(choices=[('CSE', 'Computer Science and Engineering'), ('MNC', 'Mathematics and Computing'), ('ECE', 'Electronics and Communication Engineering'), ('EEE', 'Electronics and Electrical Engineering'), ('ME', 'Mechanical Engineering'), ('CE', 'Civil Engineering'), ('CL', 'Chemical Engineering'), ('EP', 'Engineering Physics'), ('CST', 'Chemical Science and Technology'), ('BT', 'Biotechnology'), ('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Mathematics', 'Mathematics'), ('Design', 'Design'), ('Others', 'Others')], default='CSE', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='programs',
            field=models.CharField(choices=[('B.Tech', 'Bachelor of Technology'), ('B.Des', 'Bachelor of Design'), ('M.Tech', 'Master of Technology'), ('M.Des', 'Master of Design'), ('M.Sc', 'Master of Science'), ('Phd', 'PHD'), ('Others', 'Others')], default='B.Tech', max_length=5),
        ),
    ]
