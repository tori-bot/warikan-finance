# Generated by Django 4.0.5 on 2022-06-23 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance_app', '0008_bill'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='due_date',
            field=models.DateTimeField(null=True),
        ),
    ]