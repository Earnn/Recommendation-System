# Generated by Django 2.0.1 on 2018-03-20 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0026_nparray_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nparray',
            name='q_array',
        ),
    ]
