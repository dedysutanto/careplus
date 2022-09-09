# Generated by Django 4.1 on 2022-09-09 06:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import invoice.models
import modelcluster.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctor', '0001_initial'),
        ('patient', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=16, unique=True, verbose_name='ID')),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date Time')),
                ('is_final', models.BooleanField(default=False, verbose_name='Check and Correct')),
                ('is_cancel', models.BooleanField(default=False, verbose_name='Cancel')),
                ('is_email', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('doctor', models.ForeignKey(limit_choices_to=invoice.models.Invoices.limit_choices_to_current_user, on_delete=django.db.models.deletion.RESTRICT, to='doctor.doctors', verbose_name='Doctor')),
                ('patient', models.ForeignKey(limit_choices_to=invoice.models.Invoices.limit_choices_to_current_user, on_delete=django.db.models.deletion.CASCADE, to='patient.patients')),
                ('soap', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patient.soaps')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'invoice',
                'verbose_name_plural': 'invoices',
                'db_table': 'invoices',
            },
        ),
        migrations.CreateModel(
            name='InvoiceItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('item', models.CharField(max_length=50, verbose_name='Item')),
                ('quantity', models.IntegerField(default=1)),
                ('cost', models.IntegerField()),
                ('sub_total', models.IntegerField()),
                ('invoice', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_invoice', to='invoice.invoices')),
            ],
            options={
                'db_table': 'invoice_items',
            },
        ),
    ]
