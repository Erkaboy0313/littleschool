# Generated by Django 4.0.5 on 2022-06-11 05:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('schoolweb', '0007_course_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
