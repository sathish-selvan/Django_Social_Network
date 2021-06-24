# Generated by Django 3.2.3 on 2021-05-31 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_relationship'),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='usesr',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='post',
            name='liked',
            field=models.ManyToManyField(blank=True, default=None, related_name='likes', to='profiles.Profile'),
        ),
    ]