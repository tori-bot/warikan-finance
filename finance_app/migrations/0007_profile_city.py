# Generated by Django 4.0.5 on 2022-06-23 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance_app', '0006_alter_profile_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
