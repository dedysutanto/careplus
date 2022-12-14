# Generated by Django 4.1 on 2022-09-11 20:52

from django.db import migrations
import django.db.models.deletion
import invoice.models
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_alter_soaps_image'),
        ('invoice', '0002_invoices_sort_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoices',
            name='patient',
            field=modelcluster.fields.ParentalKey(limit_choices_to=invoice.models.Invoices.limit_choices_to_current_user, on_delete=django.db.models.deletion.CASCADE, related_name='related_invoice_patient', to='patient.patients'),
        ),
    ]
