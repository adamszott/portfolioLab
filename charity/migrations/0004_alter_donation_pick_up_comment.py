# Generated by Django 4.1.5 on 2023-03-17 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0003_donation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='pick_up_comment',
            field=models.CharField(max_length=500),
        ),
    ]