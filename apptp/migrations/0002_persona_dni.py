# Generated by Django 4.0.2 on 2022-02-15 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='dni',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
