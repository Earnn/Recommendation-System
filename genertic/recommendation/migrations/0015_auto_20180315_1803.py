# Generated by Django 2.0.1 on 2018-03-15 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0014_informations_breakfast'),
    ]

    operations = [
        migrations.AddField(
            model_name='informations',
            name='at',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='informations',
            name='cake',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='informations',
            name='clean',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='informations',
            name='coffee',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='informations',
            name='dessert',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='informations',
            name='diet',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='informations',
            name='dinner',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='informations',
            name='facebook',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='informations',
            name='fastfood',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='informations',
            name='grill',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='informations',
            name='instagram',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='informations',
            name='japanese',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='informations',
            name='juice',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='informations',
            name='late',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='informations',
            name='line',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='informations',
            name='location',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='informations',
            name='lunch',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='informations',
            name='price',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='informations',
            name='service',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='informations',
            name='shabu',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='informations',
            name='steak',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='informations',
            name='taste',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='informations',
            name='thai',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='informations',
            name='twitter',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='informations',
            name='breakfast',
            field=models.BooleanField(default=0),
        ),
    ]
