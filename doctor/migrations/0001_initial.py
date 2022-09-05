# Generated by Django 4.1 on 2022-09-05 13:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('phone', models.CharField(max_length=50, verbose_name='Telephone/HP')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Address')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'doctor',
                'verbose_name_plural': 'doctors',
                'db_table': 'doctor',
            },
        ),
    ]