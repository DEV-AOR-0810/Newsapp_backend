# Generated by Django 2.1.4 on 2019-06-20 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_votecomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='usergroup',
            name='pinned_commentaries',
            field=models.TextField(blank=True),
        ),
    ]