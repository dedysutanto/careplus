# Generated by Django 4.1 on 2022-09-05 03:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import modelcluster.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=3, verbose_name='Gender')),
                ('dob', models.DateField(verbose_name='Date of Birth')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Address')),
                ('phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='Telephone/HP')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'patient',
                'verbose_name_plural': 'patients',
                'db_table': 'patients',
            },
        ),
        migrations.CreateModel(
            name='TeethUpperRight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('one', models.CharField(blank=True, choices=[(None, '--'), ('AA', 'AA'), ('GR', 'GR')], default=None, max_length=2, null=True, verbose_name='1')),
                ('two', models.CharField(blank=True, choices=[(None, '--'), ('AA', 'AA'), ('GR', 'GR')], default=None, max_length=2, null=True, verbose_name='2')),
                ('three', models.CharField(blank=True, choices=[(None, '--'), ('AA', 'AA'), ('GR', 'GR')], default=None, max_length=2, null=True, verbose_name='3')),
                ('four', models.CharField(blank=True, choices=[(None, '--'), ('AA', 'AA'), ('GR', 'GR')], default=None, max_length=2, null=True, verbose_name='4')),
                ('five', models.CharField(blank=True, choices=[(None, '--'), ('AA', 'AA'), ('GR', 'GR')], default=None, max_length=2, null=True, verbose_name='5')),
                ('six', models.CharField(blank=True, choices=[(None, '--'), ('AA', 'AA'), ('GR', 'GR')], default=None, max_length=2, null=True, verbose_name='6')),
                ('seven', models.CharField(blank=True, choices=[(None, '--'), ('AA', 'AA'), ('GR', 'GR')], default=None, max_length=2, null=True, verbose_name='7')),
                ('eight', models.CharField(blank=True, choices=[(None, '--'), ('AA', 'AA'), ('GR', 'GR')], default=None, max_length=2, null=True, verbose_name='8')),
                ('m_one', models.CharField(blank=True, choices=[(None, '--'), ('AA', 'AA'), ('GR', 'GR')], default=None, max_length=2, null=True, verbose_name='I')),
                ('m_two', models.CharField(blank=True, choices=[(None, '--'), ('AA', 'AA'), ('GR', 'GR')], default=None, max_length=2, null=True, verbose_name='II')),
                ('m_three', models.CharField(blank=True, choices=[(None, '--'), ('AA', 'AA'), ('GR', 'GR')], default=None, max_length=2, null=True, verbose_name='III')),
                ('m_four', models.CharField(blank=True, choices=[(None, '--'), ('AA', 'AA'), ('GR', 'GR')], default=None, max_length=2, null=True, verbose_name='IV')),
                ('m_five', models.CharField(blank=True, choices=[(None, '--'), ('AA', 'AA'), ('GR', 'GR')], default=None, max_length=2, null=True, verbose_name='V')),
                ('patient', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='teeth_upper_right', to='patient.patients')),
            ],
            options={
                'db_table': 'teeth_upper_right',
            },
        ),
        migrations.CreateModel(
            name='TeethUpperLeft',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('one', models.CharField(blank=True, choices=[(None, '--'), ('AA', 'AA'), ('GR', 'GR')], default=None, max_length=2, null=True, verbose_name='1')),
                ('two', models.CharField(blank=True, choices=[(None, '--'), ('AA', 'AA'), ('GR', 'GR')], default=None, max_length=2, null=True, verbose_name='2')),
                ('three', models.CharField(blank=True, choices=[(None, '--'), ('AA', 'AA'), ('GR', 'GR')], default=None, max_length=2, null=True, verbose_name='3')),
                ('four', models.CharField(blank=True, choices=[(None, '--'), ('AA', 'AA'), ('GR', 'GR')], default=None, max_length=2, null=True, verbose_name='4')),
                ('five', models.CharField(blank=True, choices=[(None, '--'), ('AA', 'AA'), ('GR', 'GR')], default=None, max_length=2, null=True, verbose_name='5')),
                ('six', models.CharField(blank=True, choices=[(None, '--'), ('AA', 'AA'), ('GR', 'GR')], default=None, max_length=2, null=True, verbose_name='6')),
                ('seven', models.CharField(blank=True, choices=[(None, '--'), ('AA', 'AA'), ('GR', 'GR')], default=None, max_length=2, null=True, verbose_name='7')),
                ('eight', models.CharField(blank=True, choices=[(None, '--'), ('AA', 'AA'), ('GR', 'GR')], default=None, max_length=2, null=True, verbose_name='8')),
                ('m_one', models.CharField(blank=True, choices=[(None, '--'), ('AA', 'AA'), ('GR', 'GR')], default=None, max_length=2, null=True, verbose_name='I')),
                ('m_two', models.CharField(blank=True, choices=[(None, '--'), ('AA', 'AA'), ('GR', 'GR')], default=None, max_length=2, null=True, verbose_name='II')),
                ('m_three', models.CharField(blank=True, choices=[(None, '--'), ('AA', 'AA'), ('GR', 'GR')], default=None, max_length=2, null=True, verbose_name='III')),
                ('m_four', models.CharField(blank=True, choices=[(None, '--'), ('AA', 'AA'), ('GR', 'GR')], default=None, max_length=2, null=True, verbose_name='IV')),
                ('m_five', models.CharField(blank=True, choices=[(None, '--'), ('AA', 'AA'), ('GR', 'GR')], default=None, max_length=2, null=True, verbose_name='V')),
                ('patient', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='teeth_upper_left', to='patient.patients')),
            ],
            options={
                'db_table': 'teeth_upper_left',
            },
        ),
        migrations.CreateModel(
            name='TeethLowerRight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('one', models.CharField(blank=True, choices=[(None, '--'), ('AA', 'AA'), ('GR', 'GR')], default=None, max_length=2, null=True, verbose_name='1')),
                ('two', models.CharField(blank=True, choices=[(None, '--'), ('AA', 'AA'), ('GR', 'GR')], default=None, max_length=2, null=True, verbose_name='2')),
                ('three', models.CharField(blank=True, choices=[(None, '--'), ('AA', 'AA'), ('GR', 'GR')], default=None, max_length=2, null=True, verbose_name='3')),
                ('four', models.CharField(blank=True, choices=[(None, '--'), ('AA', 'AA'), ('GR', 'GR')], default=None, max_length=2, null=True, verbose_name='4')),
                ('five', models.CharField(blank=True, choices=[(None, '--'), ('AA', 'AA'), ('GR', 'GR')], default=None, max_length=2, null=True, verbose_name='5')),
                ('six', models.CharField(blank=True, choices=[(None, '--'), ('AA', 'AA'), ('GR', 'GR')], default=None, max_length=2, null=True, verbose_name='6')),
                ('seven', models.CharField(blank=True, choices=[(None, '--'), ('AA', 'AA'), ('GR', 'GR')], default=None, max_length=2, null=True, verbose_name='7')),
                ('eight', models.CharField(blank=True, choices=[(None, '--'), ('AA', 'AA'), ('GR', 'GR')], default=None, max_length=2, null=True, verbose_name='8')),
                ('m_one', models.CharField(blank=True, choices=[(None, '--'), ('AA', 'AA'), ('GR', 'GR')], default=None, max_length=2, null=True, verbose_name='I')),
                ('m_two', models.CharField(blank=True, choices=[(None, '--'), ('AA', 'AA'), ('GR', 'GR')], default=None, max_length=2, null=True, verbose_name='II')),
                ('m_three', models.CharField(blank=True, choices=[(None, '--'), ('AA', 'AA'), ('GR', 'GR')], default=None, max_length=2, null=True, verbose_name='III')),
                ('m_four', models.CharField(blank=True, choices=[(None, '--'), ('AA', 'AA'), ('GR', 'GR')], default=None, max_length=2, null=True, verbose_name='IV')),
                ('m_five', models.CharField(blank=True, choices=[(None, '--'), ('AA', 'AA'), ('GR', 'GR')], default=None, max_length=2, null=True, verbose_name='V')),
                ('patient', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='teeth_lower_right', to='patient.patients')),
            ],
            options={
                'db_table': 'teeth_lower_right',
            },
        ),
        migrations.CreateModel(
            name='TeethLowerLeft',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('one', models.CharField(blank=True, choices=[(None, '--'), ('AA', 'AA'), ('GR', 'GR')], default=None, max_length=2, null=True, verbose_name='1')),
                ('two', models.CharField(blank=True, choices=[(None, '--'), ('AA', 'AA'), ('GR', 'GR')], default=None, max_length=2, null=True, verbose_name='2')),
                ('three', models.CharField(blank=True, choices=[(None, '--'), ('AA', 'AA'), ('GR', 'GR')], default=None, max_length=2, null=True, verbose_name='3')),
                ('four', models.CharField(blank=True, choices=[(None, '--'), ('AA', 'AA'), ('GR', 'GR')], default=None, max_length=2, null=True, verbose_name='4')),
                ('five', models.CharField(blank=True, choices=[(None, '--'), ('AA', 'AA'), ('GR', 'GR')], default=None, max_length=2, null=True, verbose_name='5')),
                ('six', models.CharField(blank=True, choices=[(None, '--'), ('AA', 'AA'), ('GR', 'GR')], default=None, max_length=2, null=True, verbose_name='6')),
                ('seven', models.CharField(blank=True, choices=[(None, '--'), ('AA', 'AA'), ('GR', 'GR')], default=None, max_length=2, null=True, verbose_name='7')),
                ('eight', models.CharField(blank=True, choices=[(None, '--'), ('AA', 'AA'), ('GR', 'GR')], default=None, max_length=2, null=True, verbose_name='8')),
                ('m_one', models.CharField(blank=True, choices=[(None, '--'), ('AA', 'AA'), ('GR', 'GR')], default=None, max_length=2, null=True, verbose_name='I')),
                ('m_two', models.CharField(blank=True, choices=[(None, '--'), ('AA', 'AA'), ('GR', 'GR')], default=None, max_length=2, null=True, verbose_name='II')),
                ('m_three', models.CharField(blank=True, choices=[(None, '--'), ('AA', 'AA'), ('GR', 'GR')], default=None, max_length=2, null=True, verbose_name='III')),
                ('m_four', models.CharField(blank=True, choices=[(None, '--'), ('AA', 'AA'), ('GR', 'GR')], default=None, max_length=2, null=True, verbose_name='IV')),
                ('m_five', models.CharField(blank=True, choices=[(None, '--'), ('AA', 'AA'), ('GR', 'GR')], default=None, max_length=2, null=True, verbose_name='V')),
                ('patient', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='teeth_lower_left', to='patient.patients')),
            ],
            options={
                'db_table': 'teeth_lower_left',
            },
        ),
        migrations.CreateModel(
            name='Soaps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date Time')),
                ('soap', models.TextField(blank=True, default='S:\nO:\nA:\nP:', null=True, verbose_name='SOAP')),
                ('additional_info', models.TextField(blank=True, null=True, verbose_name='Additional Information')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('patient', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_patient', to='patient.patients')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'SOAP',
                'verbose_name_plural': 'SOAP',
                'db_table': 'soaps',
                'ordering': ['-datetime'],
            },
        ),
    ]
