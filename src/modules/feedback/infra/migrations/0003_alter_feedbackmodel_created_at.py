# Generated by Django 5.1.1 on 2024-09-28 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_alter_feedbackmodel_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbackmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='created_at'),
        ),
    ]
