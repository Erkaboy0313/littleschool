# Generated by Django 4.0.5 on 2022-06-11 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolweb', '0006_staf_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='cost',
            field=models.IntegerField(default=0),
        ),
    ]