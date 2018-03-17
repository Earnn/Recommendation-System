# Generated by Django 2.0.1 on 2018-03-16 19:03

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recommendation', '0022_user_session'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=500), blank=True, null=True, size=None)),
                ('amount', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=500), blank=True, null=True, size=None)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('store', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='recommendation.Store')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]