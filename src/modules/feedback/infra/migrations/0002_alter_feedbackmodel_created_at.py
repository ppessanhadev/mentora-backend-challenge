# Generated by Django 5.1.1 on 2024-09-28 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbackmodel',
            name='created_at',
            field=models.DateTimeField(auto_created=True, verbose_name='created_at'),
        ),
    ]
