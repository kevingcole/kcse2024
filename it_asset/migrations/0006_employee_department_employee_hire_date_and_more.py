# Generated by Django 5.1.7 on 2025-03-26 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('it_asset', '0005_alter_profile_first_name_alter_profile_last_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='department',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='hire_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='position',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
