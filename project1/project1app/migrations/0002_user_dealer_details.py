# Generated by Django 5.0.3 on 2024-04-15 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project1app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dealer_details',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]