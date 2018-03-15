# Generated by Django 2.0.1 on 2018-03-15 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0018_auto_20180315_1810'),
    ]

    operations = [
        migrations.RenameField(
            model_name='informations',
            old_name='at',
            new_name='cake',
        ),
        migrations.RenameField(
            model_name='informations',
            old_name='clean',
            new_name='coffee',
        ),
        migrations.RenameField(
            model_name='informations',
            old_name='facebook',
            new_name='dessert',
        ),
        migrations.RenameField(
            model_name='informations',
            old_name='instagram',
            new_name='diet',
        ),
        migrations.RenameField(
            model_name='informations',
            old_name='line',
            new_name='fastfood',
        ),
        migrations.RenameField(
            model_name='informations',
            old_name='location',
            new_name='grill',
        ),
        migrations.RenameField(
            model_name='informations',
            old_name='price',
            new_name='japanese',
        ),
        migrations.RenameField(
            model_name='informations',
            old_name='service',
            new_name='juice',
        ),
        migrations.RenameField(
            model_name='informations',
            old_name='taste',
            new_name='shabu',
        ),
        migrations.RenameField(
            model_name='informations',
            old_name='twitter',
            new_name='steak',
        ),
        migrations.AddField(
            model_name='informations',
            name='thai',
            field=models.BooleanField(default=0),
        ),
    ]
