# Generated by Django 4.1.2 on 2022-11-10 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0005_remove_game_rating_remove_game_ratingqty_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='rawgID',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]