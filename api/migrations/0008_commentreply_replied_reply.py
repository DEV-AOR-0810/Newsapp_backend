# Generated by Django 2.1.4 on 2019-06-29 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_profile_uid'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentreply',
            name='replied_reply',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.CommentReply'),
        ),
    ]
