# Generated by Django 2.1.4 on 2019-06-30 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_profile_show_articles_first'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='kind',
            field=models.IntegerField(default=0),
        ),
    ]
