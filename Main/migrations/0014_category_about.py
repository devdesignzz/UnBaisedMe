# Generated by Django 3.1.5 on 2022-11-30 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0013_auto_20221130_0618'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='about',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]