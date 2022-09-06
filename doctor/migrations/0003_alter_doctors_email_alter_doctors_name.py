# Generated by Django 4.1 on 2022-09-06 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_alter_doctors_email_alter_doctors_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
    ]
