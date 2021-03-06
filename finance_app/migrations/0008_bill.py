# Generated by Django 4.0.5 on 2022-06-23 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance_app', '0007_profile_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('weekly', 'weekly'), ('2 weeks', '2 weeks'), ('monthly', 'monthly'), ('quarterly', 'quarterly'), ('6 months', '6 months'), ('annually', 'annually')], default='monthly', max_length=30, null=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('amount', models.IntegerField()),
                ('description', models.TextField()),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='finance_app.account')),
            ],
        ),
    ]
