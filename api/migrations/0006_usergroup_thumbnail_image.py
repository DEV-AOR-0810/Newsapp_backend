# Generated by Django 2.1.4 on 2019-06-27 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_usergroup_pinned_commentaries'),
    ]

    operations = [
        migrations.AddField(
            model_name='usergroup',
            name='thumbnail_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
