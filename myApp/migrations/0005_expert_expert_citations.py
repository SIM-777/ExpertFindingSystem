# Generated by Django 4.1.3 on 2023-06-10 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0004_expert_expert_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='expert',
            name='expert_citations',
            field=models.IntegerField(null=True),
        ),
    ]
