# Generated by Django 4.1 on 2022-09-05 07:03

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0024_index_image_file_hash'),
        ('patient', '0002_alter_patients_user_alter_soaps_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teethlowerleft',
            name='eight',
            field=models.CharField(blank=True, choices=[(None, '--'), ('KE', 'KE'), ('KD', 'KD'), ('KP', 'KP'), ('RG', 'RG'), ('AF', 'AF'), ('CF', 'CF'), ('GR', 'GR'), ('GP', 'GP'), ('PL', 'PL'), ('IM', 'IM'), ('In', 'In'), ('On', 'On'), ('Ab', 'Ab'), ('Cr', 'Cr'), ('Br', 'Br'), ('Ve', 'Ve'), ('M', 'M'), ('P', 'P')], default=None, max_length=2, null=True, verbose_name='8'),
        ),
        migrations.AlterField(
            model_name='teethlowerleft',
            name='five',
            field=models.CharField(blank=True, choices=[(None, '--'), ('KE', 'KE'), ('KD', 'KD'), ('KP', 'KP'), ('RG', 'RG'), ('AF', 'AF'), ('CF', 'CF'), ('GR', 'GR'), ('GP', 'GP'), ('PL', 'PL'), ('IM', 'IM'), ('In', 'In'), ('On', 'On'), ('Ab', 'Ab'), ('Cr', 'Cr'), ('Br', 'Br'), ('Ve', 'Ve'), ('M', 'M'), ('P', 'P')], default=None, max_length=2, null=True, verbose_name='5'),
        ),
        migrations.AlterField(
            model_name='teethlowerleft',
            name='four',
            field=models.CharField(blank=True, choices=[(None, '--'), ('KE', 'KE'), ('KD', 'KD'), ('KP', 'KP'), ('RG', 'RG'), ('AF', 'AF'), ('CF', 'CF'), ('GR', 'GR'), ('GP', 'GP'), ('PL', 'PL'), ('IM', 'IM'), ('In', 'In'), ('On', 'On'), ('Ab', 'Ab'), ('Cr', 'Cr'), ('Br', 'Br'), ('Ve', 'Ve'), ('M', 'M'), ('P', 'P')], default=None, max_length=2, null=True, verbose_name='4'),
        ),
        migrations.AlterField(
            model_name='teethlowerleft',
            name='m_five',
            field=models.CharField(blank=True, choices=[(None, '--'), ('KE', 'KE'), ('KD', 'KD'), ('KP', 'KP'), ('RG', 'RG'), ('AF', 'AF'), ('CF', 'CF'), ('GR', 'GR'), ('GP', 'GP'), ('PL', 'PL'), ('IM', 'IM'), ('In', 'In'), ('On', 'On'), ('Ab', 'Ab'), ('Cr', 'Cr'), ('Br', 'Br'), ('Ve', 'Ve'), ('M', 'M'), ('P', 'P')], default=None, max_length=2, null=True, verbose_name='V'),
        ),
        migrations.AlterField(
            model_name='teethlowerleft',
            name='m_four',
            field=models.CharField(blank=True, choices=[(None, '--'), ('KE', 'KE'), ('KD', 'KD'), ('KP', 'KP'), ('RG', 'RG'), ('AF', 'AF'), ('CF', 'CF'), ('GR', 'GR'), ('GP', 'GP'), ('PL', 'PL'), ('IM', 'IM'), ('In', 'In'), ('On', 'On'), ('Ab', 'Ab'), ('Cr', 'Cr'), ('Br', 'Br'), ('Ve', 'Ve'), ('M', 'M'), ('P', 'P')], default=None, max_length=2, null=True, verbose_name='IV'),
        ),
        migrations.AlterField(
            model_name='teethlowerleft',
            name='m_one',
            field=models.CharField(blank=True, choices=[(None, '--'), ('KE', 'KE'), ('KD', 'KD'), ('KP', 'KP'), ('RG', 'RG'), ('AF', 'AF'), ('CF', 'CF'), ('GR', 'GR'), ('GP', 'GP'), ('PL', 'PL'), ('IM', 'IM'), ('In', 'In'), ('On', 'On'), ('Ab', 'Ab'), ('Cr', 'Cr'), ('Br', 'Br'), ('Ve', 'Ve'), ('M', 'M'), ('P', 'P')], default=None, max_length=2, null=True, verbose_name='I'),
        ),
        migrations.AlterField(
            model_name='teethlowerleft',
            name='m_three',
            field=models.CharField(blank=True, choices=[(None, '--'), ('KE', 'KE'), ('KD', 'KD'), ('KP', 'KP'), ('RG', 'RG'), ('AF', 'AF'), ('CF', 'CF'), ('GR', 'GR'), ('GP', 'GP'), ('PL', 'PL'), ('IM', 'IM'), ('In', 'In'), ('On', 'On'), ('Ab', 'Ab'), ('Cr', 'Cr'), ('Br', 'Br'), ('Ve', 'Ve'), ('M', 'M'), ('P', 'P')], default=None, max_length=2, null=True, verbose_name='III'),
        ),
        migrations.AlterField(
            model_name='teethlowerleft',
            name='m_two',
            field=models.CharField(blank=True, choices=[(None, '--'), ('KE', 'KE'), ('KD', 'KD'), ('KP', 'KP'), ('RG', 'RG'), ('AF', 'AF'), ('CF', 'CF'), ('GR', 'GR'), ('GP', 'GP'), ('PL', 'PL'), ('IM', 'IM'), ('In', 'In'), ('On', 'On'), ('Ab', 'Ab'), ('Cr', 'Cr'), ('Br', 'Br'), ('Ve', 'Ve'), ('M', 'M'), ('P', 'P')], default=None, max_length=2, null=True, verbose_name='II'),
        ),
        migrations.AlterField(
            model_name='teethlowerleft',
            name='one',
            field=models.CharField(blank=True, choices=[(None, '--'), ('KE', 'KE'), ('KD', 'KD'), ('KP', 'KP'), ('RG', 'RG'), ('AF', 'AF'), ('CF', 'CF'), ('GR', 'GR'), ('GP', 'GP'), ('PL', 'PL'), ('IM', 'IM'), ('In', 'In'), ('On', 'On'), ('Ab', 'Ab'), ('Cr', 'Cr'), ('Br', 'Br'), ('Ve', 'Ve'), ('M', 'M'), ('P', 'P')], default=None, max_length=2, null=True, verbose_name='1'),
        ),
        migrations.AlterField(
            model_name='teethlowerleft',
            name='seven',
            field=models.CharField(blank=True, choices=[(None, '--'), ('KE', 'KE'), ('KD', 'KD'), ('KP', 'KP'), ('RG', 'RG'), ('AF', 'AF'), ('CF', 'CF'), ('GR', 'GR'), ('GP', 'GP'), ('PL', 'PL'), ('IM', 'IM'), ('In', 'In'), ('On', 'On'), ('Ab', 'Ab'), ('Cr', 'Cr'), ('Br', 'Br'), ('Ve', 'Ve'), ('M', 'M'), ('P', 'P')], default=None, max_length=2, null=True, verbose_name='7'),
        ),
        migrations.AlterField(
            model_name='teethlowerleft',
            name='six',
            field=models.CharField(blank=True, choices=[(None, '--'), ('KE', 'KE'), ('KD', 'KD'), ('KP', 'KP'), ('RG', 'RG'), ('AF', 'AF'), ('CF', 'CF'), ('GR', 'GR'), ('GP', 'GP'), ('PL', 'PL'), ('IM', 'IM'), ('In', 'In'), ('On', 'On'), ('Ab', 'Ab'), ('Cr', 'Cr'), ('Br', 'Br'), ('Ve', 'Ve'), ('M', 'M'), ('P', 'P')], default=None, max_length=2, null=True, verbose_name='6'),
        ),
        migrations.AlterField(
            model_name='teethlowerleft',
            name='three',
            field=models.CharField(blank=True, choices=[(None, '--'), ('KE', 'KE'), ('KD', 'KD'), ('KP', 'KP'), ('RG', 'RG'), ('AF', 'AF'), ('CF', 'CF'), ('GR', 'GR'), ('GP', 'GP'), ('PL', 'PL'), ('IM', 'IM'), ('In', 'In'), ('On', 'On'), ('Ab', 'Ab'), ('Cr', 'Cr'), ('Br', 'Br'), ('Ve', 'Ve'), ('M', 'M'), ('P', 'P')], default=None, max_length=2, null=True, verbose_name='3'),
        ),
        migrations.AlterField(
            model_name='teethlowerleft',
            name='two',
            field=models.CharField(blank=True, choices=[(None, '--'), ('KE', 'KE'), ('KD', 'KD'), ('KP', 'KP'), ('RG', 'RG'), ('AF', 'AF'), ('CF', 'CF'), ('GR', 'GR'), ('GP', 'GP'), ('PL', 'PL'), ('IM', 'IM'), ('In', 'In'), ('On', 'On'), ('Ab', 'Ab'), ('Cr', 'Cr'), ('Br', 'Br'), ('Ve', 'Ve'), ('M', 'M'), ('P', 'P')], default=None, max_length=2, null=True, verbose_name='2'),
        ),
        migrations.AlterField(
            model_name='teethlowerright',
            name='eight',
            field=models.CharField(blank=True, choices=[(None, '--'), ('KE', 'KE'), ('KD', 'KD'), ('KP', 'KP'), ('RG', 'RG'), ('AF', 'AF'), ('CF', 'CF'), ('GR', 'GR'), ('GP', 'GP'), ('PL', 'PL'), ('IM', 'IM'), ('In', 'In'), ('On', 'On'), ('Ab', 'Ab'), ('Cr', 'Cr'), ('Br', 'Br'), ('Ve', 'Ve'), ('M', 'M'), ('P', 'P')], default=None, max_length=2, null=True, verbose_name='8'),
        ),
        migrations.AlterField(
            model_name='teethlowerright',
            name='five',
            field=models.CharField(blank=True, choices=[(None, '--'), ('KE', 'KE'), ('KD', 'KD'), ('KP', 'KP'), ('RG', 'RG'), ('AF', 'AF'), ('CF', 'CF'), ('GR', 'GR'), ('GP', 'GP'), ('PL', 'PL'), ('IM', 'IM'), ('In', 'In'), ('On', 'On'), ('Ab', 'Ab'), ('Cr', 'Cr'), ('Br', 'Br'), ('Ve', 'Ve'), ('M', 'M'), ('P', 'P')], default=None, max_length=2, null=True, verbose_name='5'),
        ),
        migrations.AlterField(
            model_name='teethlowerright',
            name='four',
            field=models.CharField(blank=True, choices=[(None, '--'), ('KE', 'KE'), ('KD', 'KD'), ('KP', 'KP'), ('RG', 'RG'), ('AF', 'AF'), ('CF', 'CF'), ('GR', 'GR'), ('GP', 'GP'), ('PL', 'PL'), ('IM', 'IM'), ('In', 'In'), ('On', 'On'), ('Ab', 'Ab'), ('Cr', 'Cr'), ('Br', 'Br'), ('Ve', 'Ve'), ('M', 'M'), ('P', 'P')], default=None, max_length=2, null=True, verbose_name='4'),
        ),
        migrations.AlterField(
            model_name='teethlowerright',
            name='m_five',
            field=models.CharField(blank=True, choices=[(None, '--'), ('KE', 'KE'), ('KD', 'KD'), ('KP', 'KP'), ('RG', 'RG'), ('AF', 'AF'), ('CF', 'CF'), ('GR', 'GR'), ('GP', 'GP'), ('PL', 'PL'), ('IM', 'IM'), ('In', 'In'), ('On', 'On'), ('Ab', 'Ab'), ('Cr', 'Cr'), ('Br', 'Br'), ('Ve', 'Ve'), ('M', 'M'), ('P', 'P')], default=None, max_length=2, null=True, verbose_name='V'),
        ),
        migrations.AlterField(
            model_name='teethlowerright',
            name='m_four',
            field=models.CharField(blank=True, choices=[(None, '--'), ('KE', 'KE'), ('KD', 'KD'), ('KP', 'KP'), ('RG', 'RG'), ('AF', 'AF'), ('CF', 'CF'), ('GR', 'GR'), ('GP', 'GP'), ('PL', 'PL'), ('IM', 'IM'), ('In', 'In'), ('On', 'On'), ('Ab', 'Ab'), ('Cr', 'Cr'), ('Br', 'Br'), ('Ve', 'Ve'), ('M', 'M'), ('P', 'P')], default=None, max_length=2, null=True, verbose_name='IV'),
        ),
        migrations.AlterField(
            model_name='teethlowerright',
            name='m_one',
            field=models.CharField(blank=True, choices=[(None, '--'), ('KE', 'KE'), ('KD', 'KD'), ('KP', 'KP'), ('RG', 'RG'), ('AF', 'AF'), ('CF', 'CF'), ('GR', 'GR'), ('GP', 'GP'), ('PL', 'PL'), ('IM', 'IM'), ('In', 'In'), ('On', 'On'), ('Ab', 'Ab'), ('Cr', 'Cr'), ('Br', 'Br'), ('Ve', 'Ve'), ('M', 'M'), ('P', 'P')], default=None, max_length=2, null=True, verbose_name='I'),
        ),
        migrations.AlterField(
            model_name='teethlowerright',
            name='m_three',
            field=models.CharField(blank=True, choices=[(None, '--'), ('KE', 'KE'), ('KD', 'KD'), ('KP', 'KP'), ('RG', 'RG'), ('AF', 'AF'), ('CF', 'CF'), ('GR', 'GR'), ('GP', 'GP'), ('PL', 'PL'), ('IM', 'IM'), ('In', 'In'), ('On', 'On'), ('Ab', 'Ab'), ('Cr', 'Cr'), ('Br', 'Br'), ('Ve', 'Ve'), ('M', 'M'), ('P', 'P')], default=None, max_length=2, null=True, verbose_name='III'),
        ),
        migrations.AlterField(
            model_name='teethlowerright',
            name='m_two',
            field=models.CharField(blank=True, choices=[(None, '--'), ('KE', 'KE'), ('KD', 'KD'), ('KP', 'KP'), ('RG', 'RG'), ('AF', 'AF'), ('CF', 'CF'), ('GR', 'GR'), ('GP', 'GP'), ('PL', 'PL'), ('IM', 'IM'), ('In', 'In'), ('On', 'On'), ('Ab', 'Ab'), ('Cr', 'Cr'), ('Br', 'Br'), ('Ve', 'Ve'), ('M', 'M'), ('P', 'P')], default=None, max_length=2, null=True, verbose_name='II'),
        ),
        migrations.AlterField(
            model_name='teethlowerright',
            name='one',
            field=models.CharField(blank=True, choices=[(None, '--'), ('KE', 'KE'), ('KD', 'KD'), ('KP', 'KP'), ('RG', 'RG'), ('AF', 'AF'), ('CF', 'CF'), ('GR', 'GR'), ('GP', 'GP'), ('PL', 'PL'), ('IM', 'IM'), ('In', 'In'), ('On', 'On'), ('Ab', 'Ab'), ('Cr', 'Cr'), ('Br', 'Br'), ('Ve', 'Ve'), ('M', 'M'), ('P', 'P')], default=None, max_length=2, null=True, verbose_name='1'),
        ),
        migrations.AlterField(
            model_name='teethlowerright',
            name='seven',
            field=models.CharField(blank=True, choices=[(None, '--'), ('KE', 'KE'), ('KD', 'KD'), ('KP', 'KP'), ('RG', 'RG'), ('AF', 'AF'), ('CF', 'CF'), ('GR', 'GR'), ('GP', 'GP'), ('PL', 'PL'), ('IM', 'IM'), ('In', 'In'), ('On', 'On'), ('Ab', 'Ab'), ('Cr', 'Cr'), ('Br', 'Br'), ('Ve', 'Ve'), ('M', 'M'), ('P', 'P')], default=None, max_length=2, null=True, verbose_name='7'),
        ),
        migrations.AlterField(
            model_name='teethlowerright',
            name='six',
            field=models.CharField(blank=True, choices=[(None, '--'), ('KE', 'KE'), ('KD', 'KD'), ('KP', 'KP'), ('RG', 'RG'), ('AF', 'AF'), ('CF', 'CF'), ('GR', 'GR'), ('GP', 'GP'), ('PL', 'PL'), ('IM', 'IM'), ('In', 'In'), ('On', 'On'), ('Ab', 'Ab'), ('Cr', 'Cr'), ('Br', 'Br'), ('Ve', 'Ve'), ('M', 'M'), ('P', 'P')], default=None, max_length=2, null=True, verbose_name='6'),
        ),
        migrations.AlterField(
            model_name='teethlowerright',
            name='three',
            field=models.CharField(blank=True, choices=[(None, '--'), ('KE', 'KE'), ('KD', 'KD'), ('KP', 'KP'), ('RG', 'RG'), ('AF', 'AF'), ('CF', 'CF'), ('GR', 'GR'), ('GP', 'GP'), ('PL', 'PL'), ('IM', 'IM'), ('In', 'In'), ('On', 'On'), ('Ab', 'Ab'), ('Cr', 'Cr'), ('Br', 'Br'), ('Ve', 'Ve'), ('M', 'M'), ('P', 'P')], default=None, max_length=2, null=True, verbose_name='3'),
        ),
        migrations.AlterField(
            model_name='teethlowerright',
            name='two',
            field=models.CharField(blank=True, choices=[(None, '--'), ('KE', 'KE'), ('KD', 'KD'), ('KP', 'KP'), ('RG', 'RG'), ('AF', 'AF'), ('CF', 'CF'), ('GR', 'GR'), ('GP', 'GP'), ('PL', 'PL'), ('IM', 'IM'), ('In', 'In'), ('On', 'On'), ('Ab', 'Ab'), ('Cr', 'Cr'), ('Br', 'Br'), ('Ve', 'Ve'), ('M', 'M'), ('P', 'P')], default=None, max_length=2, null=True, verbose_name='2'),
        ),
        migrations.AlterField(
            model_name='teethupperleft',
            name='eight',
            field=models.CharField(blank=True, choices=[(None, '--'), ('KE', 'KE'), ('KD', 'KD'), ('KP', 'KP'), ('RG', 'RG'), ('AF', 'AF'), ('CF', 'CF'), ('GR', 'GR'), ('GP', 'GP'), ('PL', 'PL'), ('IM', 'IM'), ('In', 'In'), ('On', 'On'), ('Ab', 'Ab'), ('Cr', 'Cr'), ('Br', 'Br'), ('Ve', 'Ve'), ('M', 'M'), ('P', 'P')], default=None, max_length=2, null=True, verbose_name='8'),
        ),
        migrations.AlterField(
            model_name='teethupperleft',
            name='five',
            field=models.CharField(blank=True, choices=[(None, '--'), ('KE', 'KE'), ('KD', 'KD'), ('KP', 'KP'), ('RG', 'RG'), ('AF', 'AF'), ('CF', 'CF'), ('GR', 'GR'), ('GP', 'GP'), ('PL', 'PL'), ('IM', 'IM'), ('In', 'In'), ('On', 'On'), ('Ab', 'Ab'), ('Cr', 'Cr'), ('Br', 'Br'), ('Ve', 'Ve'), ('M', 'M'), ('P', 'P')], default=None, max_length=2, null=True, verbose_name='5'),
        ),
        migrations.AlterField(
            model_name='teethupperleft',
            name='four',
            field=models.CharField(blank=True, choices=[(None, '--'), ('KE', 'KE'), ('KD', 'KD'), ('KP', 'KP'), ('RG', 'RG'), ('AF', 'AF'), ('CF', 'CF'), ('GR', 'GR'), ('GP', 'GP'), ('PL', 'PL'), ('IM', 'IM'), ('In', 'In'), ('On', 'On'), ('Ab', 'Ab'), ('Cr', 'Cr'), ('Br', 'Br'), ('Ve', 'Ve'), ('M', 'M'), ('P', 'P')], default=None, max_length=2, null=True, verbose_name='4'),
        ),
        migrations.AlterField(
            model_name='teethupperleft',
            name='m_five',
            field=models.CharField(blank=True, choices=[(None, '--'), ('KE', 'KE'), ('KD', 'KD'), ('KP', 'KP'), ('RG', 'RG'), ('AF', 'AF'), ('CF', 'CF'), ('GR', 'GR'), ('GP', 'GP'), ('PL', 'PL'), ('IM', 'IM'), ('In', 'In'), ('On', 'On'), ('Ab', 'Ab'), ('Cr', 'Cr'), ('Br', 'Br'), ('Ve', 'Ve'), ('M', 'M'), ('P', 'P')], default=None, max_length=2, null=True, verbose_name='V'),
        ),
        migrations.AlterField(
            model_name='teethupperleft',
            name='m_four',
            field=models.CharField(blank=True, choices=[(None, '--'), ('KE', 'KE'), ('KD', 'KD'), ('KP', 'KP'), ('RG', 'RG'), ('AF', 'AF'), ('CF', 'CF'), ('GR', 'GR'), ('GP', 'GP'), ('PL', 'PL'), ('IM', 'IM'), ('In', 'In'), ('On', 'On'), ('Ab', 'Ab'), ('Cr', 'Cr'), ('Br', 'Br'), ('Ve', 'Ve'), ('M', 'M'), ('P', 'P')], default=None, max_length=2, null=True, verbose_name='IV'),
        ),
        migrations.AlterField(
            model_name='teethupperleft',
            name='m_one',
            field=models.CharField(blank=True, choices=[(None, '--'), ('KE', 'KE'), ('KD', 'KD'), ('KP', 'KP'), ('RG', 'RG'), ('AF', 'AF'), ('CF', 'CF'), ('GR', 'GR'), ('GP', 'GP'), ('PL', 'PL'), ('IM', 'IM'), ('In', 'In'), ('On', 'On'), ('Ab', 'Ab'), ('Cr', 'Cr'), ('Br', 'Br'), ('Ve', 'Ve'), ('M', 'M'), ('P', 'P')], default=None, max_length=2, null=True, verbose_name='I'),
        ),
        migrations.AlterField(
            model_name='teethupperleft',
            name='m_three',
            field=models.CharField(blank=True, choices=[(None, '--'), ('KE', 'KE'), ('KD', 'KD'), ('KP', 'KP'), ('RG', 'RG'), ('AF', 'AF'), ('CF', 'CF'), ('GR', 'GR'), ('GP', 'GP'), ('PL', 'PL'), ('IM', 'IM'), ('In', 'In'), ('On', 'On'), ('Ab', 'Ab'), ('Cr', 'Cr'), ('Br', 'Br'), ('Ve', 'Ve'), ('M', 'M'), ('P', 'P')], default=None, max_length=2, null=True, verbose_name='III'),
        ),
        migrations.AlterField(
            model_name='teethupperleft',
            name='m_two',
            field=models.CharField(blank=True, choices=[(None, '--'), ('KE', 'KE'), ('KD', 'KD'), ('KP', 'KP'), ('RG', 'RG'), ('AF', 'AF'), ('CF', 'CF'), ('GR', 'GR'), ('GP', 'GP'), ('PL', 'PL'), ('IM', 'IM'), ('In', 'In'), ('On', 'On'), ('Ab', 'Ab'), ('Cr', 'Cr'), ('Br', 'Br'), ('Ve', 'Ve'), ('M', 'M'), ('P', 'P')], default=None, max_length=2, null=True, verbose_name='II'),
        ),
        migrations.AlterField(
            model_name='teethupperleft',
            name='one',
            field=models.CharField(blank=True, choices=[(None, '--'), ('KE', 'KE'), ('KD', 'KD'), ('KP', 'KP'), ('RG', 'RG'), ('AF', 'AF'), ('CF', 'CF'), ('GR', 'GR'), ('GP', 'GP'), ('PL', 'PL'), ('IM', 'IM'), ('In', 'In'), ('On', 'On'), ('Ab', 'Ab'), ('Cr', 'Cr'), ('Br', 'Br'), ('Ve', 'Ve'), ('M', 'M'), ('P', 'P')], default=None, max_length=2, null=True, verbose_name='1'),
        ),
        migrations.AlterField(
            model_name='teethupperleft',
            name='seven',
            field=models.CharField(blank=True, choices=[(None, '--'), ('KE', 'KE'), ('KD', 'KD'), ('KP', 'KP'), ('RG', 'RG'), ('AF', 'AF'), ('CF', 'CF'), ('GR', 'GR'), ('GP', 'GP'), ('PL', 'PL'), ('IM', 'IM'), ('In', 'In'), ('On', 'On'), ('Ab', 'Ab'), ('Cr', 'Cr'), ('Br', 'Br'), ('Ve', 'Ve'), ('M', 'M'), ('P', 'P')], default=None, max_length=2, null=True, verbose_name='7'),
        ),
        migrations.AlterField(
            model_name='teethupperleft',
            name='six',
            field=models.CharField(blank=True, choices=[(None, '--'), ('KE', 'KE'), ('KD', 'KD'), ('KP', 'KP'), ('RG', 'RG'), ('AF', 'AF'), ('CF', 'CF'), ('GR', 'GR'), ('GP', 'GP'), ('PL', 'PL'), ('IM', 'IM'), ('In', 'In'), ('On', 'On'), ('Ab', 'Ab'), ('Cr', 'Cr'), ('Br', 'Br'), ('Ve', 'Ve'), ('M', 'M'), ('P', 'P')], default=None, max_length=2, null=True, verbose_name='6'),
        ),
        migrations.AlterField(
            model_name='teethupperleft',
            name='three',
            field=models.CharField(blank=True, choices=[(None, '--'), ('KE', 'KE'), ('KD', 'KD'), ('KP', 'KP'), ('RG', 'RG'), ('AF', 'AF'), ('CF', 'CF'), ('GR', 'GR'), ('GP', 'GP'), ('PL', 'PL'), ('IM', 'IM'), ('In', 'In'), ('On', 'On'), ('Ab', 'Ab'), ('Cr', 'Cr'), ('Br', 'Br'), ('Ve', 'Ve'), ('M', 'M'), ('P', 'P')], default=None, max_length=2, null=True, verbose_name='3'),
        ),
        migrations.AlterField(
            model_name='teethupperleft',
            name='two',
            field=models.CharField(blank=True, choices=[(None, '--'), ('KE', 'KE'), ('KD', 'KD'), ('KP', 'KP'), ('RG', 'RG'), ('AF', 'AF'), ('CF', 'CF'), ('GR', 'GR'), ('GP', 'GP'), ('PL', 'PL'), ('IM', 'IM'), ('In', 'In'), ('On', 'On'), ('Ab', 'Ab'), ('Cr', 'Cr'), ('Br', 'Br'), ('Ve', 'Ve'), ('M', 'M'), ('P', 'P')], default=None, max_length=2, null=True, verbose_name='2'),
        ),
        migrations.AlterField(
            model_name='teethupperright',
            name='eight',
            field=models.CharField(blank=True, choices=[(None, '--'), ('KE', 'KE'), ('KD', 'KD'), ('KP', 'KP'), ('RG', 'RG'), ('AF', 'AF'), ('CF', 'CF'), ('GR', 'GR'), ('GP', 'GP'), ('PL', 'PL'), ('IM', 'IM'), ('In', 'In'), ('On', 'On'), ('Ab', 'Ab'), ('Cr', 'Cr'), ('Br', 'Br'), ('Ve', 'Ve'), ('M', 'M'), ('P', 'P')], default=None, max_length=2, null=True, verbose_name='8'),
        ),
        migrations.AlterField(
            model_name='teethupperright',
            name='five',
            field=models.CharField(blank=True, choices=[(None, '--'), ('KE', 'KE'), ('KD', 'KD'), ('KP', 'KP'), ('RG', 'RG'), ('AF', 'AF'), ('CF', 'CF'), ('GR', 'GR'), ('GP', 'GP'), ('PL', 'PL'), ('IM', 'IM'), ('In', 'In'), ('On', 'On'), ('Ab', 'Ab'), ('Cr', 'Cr'), ('Br', 'Br'), ('Ve', 'Ve'), ('M', 'M'), ('P', 'P')], default=None, max_length=2, null=True, verbose_name='5'),
        ),
        migrations.AlterField(
            model_name='teethupperright',
            name='four',
            field=models.CharField(blank=True, choices=[(None, '--'), ('KE', 'KE'), ('KD', 'KD'), ('KP', 'KP'), ('RG', 'RG'), ('AF', 'AF'), ('CF', 'CF'), ('GR', 'GR'), ('GP', 'GP'), ('PL', 'PL'), ('IM', 'IM'), ('In', 'In'), ('On', 'On'), ('Ab', 'Ab'), ('Cr', 'Cr'), ('Br', 'Br'), ('Ve', 'Ve'), ('M', 'M'), ('P', 'P')], default=None, max_length=2, null=True, verbose_name='4'),
        ),
        migrations.AlterField(
            model_name='teethupperright',
            name='m_five',
            field=models.CharField(blank=True, choices=[(None, '--'), ('KE', 'KE'), ('KD', 'KD'), ('KP', 'KP'), ('RG', 'RG'), ('AF', 'AF'), ('CF', 'CF'), ('GR', 'GR'), ('GP', 'GP'), ('PL', 'PL'), ('IM', 'IM'), ('In', 'In'), ('On', 'On'), ('Ab', 'Ab'), ('Cr', 'Cr'), ('Br', 'Br'), ('Ve', 'Ve'), ('M', 'M'), ('P', 'P')], default=None, max_length=2, null=True, verbose_name='V'),
        ),
        migrations.AlterField(
            model_name='teethupperright',
            name='m_four',
            field=models.CharField(blank=True, choices=[(None, '--'), ('KE', 'KE'), ('KD', 'KD'), ('KP', 'KP'), ('RG', 'RG'), ('AF', 'AF'), ('CF', 'CF'), ('GR', 'GR'), ('GP', 'GP'), ('PL', 'PL'), ('IM', 'IM'), ('In', 'In'), ('On', 'On'), ('Ab', 'Ab'), ('Cr', 'Cr'), ('Br', 'Br'), ('Ve', 'Ve'), ('M', 'M'), ('P', 'P')], default=None, max_length=2, null=True, verbose_name='IV'),
        ),
        migrations.AlterField(
            model_name='teethupperright',
            name='m_one',
            field=models.CharField(blank=True, choices=[(None, '--'), ('KE', 'KE'), ('KD', 'KD'), ('KP', 'KP'), ('RG', 'RG'), ('AF', 'AF'), ('CF', 'CF'), ('GR', 'GR'), ('GP', 'GP'), ('PL', 'PL'), ('IM', 'IM'), ('In', 'In'), ('On', 'On'), ('Ab', 'Ab'), ('Cr', 'Cr'), ('Br', 'Br'), ('Ve', 'Ve'), ('M', 'M'), ('P', 'P')], default=None, max_length=2, null=True, verbose_name='I'),
        ),
        migrations.AlterField(
            model_name='teethupperright',
            name='m_three',
            field=models.CharField(blank=True, choices=[(None, '--'), ('KE', 'KE'), ('KD', 'KD'), ('KP', 'KP'), ('RG', 'RG'), ('AF', 'AF'), ('CF', 'CF'), ('GR', 'GR'), ('GP', 'GP'), ('PL', 'PL'), ('IM', 'IM'), ('In', 'In'), ('On', 'On'), ('Ab', 'Ab'), ('Cr', 'Cr'), ('Br', 'Br'), ('Ve', 'Ve'), ('M', 'M'), ('P', 'P')], default=None, max_length=2, null=True, verbose_name='III'),
        ),
        migrations.AlterField(
            model_name='teethupperright',
            name='m_two',
            field=models.CharField(blank=True, choices=[(None, '--'), ('KE', 'KE'), ('KD', 'KD'), ('KP', 'KP'), ('RG', 'RG'), ('AF', 'AF'), ('CF', 'CF'), ('GR', 'GR'), ('GP', 'GP'), ('PL', 'PL'), ('IM', 'IM'), ('In', 'In'), ('On', 'On'), ('Ab', 'Ab'), ('Cr', 'Cr'), ('Br', 'Br'), ('Ve', 'Ve'), ('M', 'M'), ('P', 'P')], default=None, max_length=2, null=True, verbose_name='II'),
        ),
        migrations.AlterField(
            model_name='teethupperright',
            name='one',
            field=models.CharField(blank=True, choices=[(None, '--'), ('KE', 'KE'), ('KD', 'KD'), ('KP', 'KP'), ('RG', 'RG'), ('AF', 'AF'), ('CF', 'CF'), ('GR', 'GR'), ('GP', 'GP'), ('PL', 'PL'), ('IM', 'IM'), ('In', 'In'), ('On', 'On'), ('Ab', 'Ab'), ('Cr', 'Cr'), ('Br', 'Br'), ('Ve', 'Ve'), ('M', 'M'), ('P', 'P')], default=None, max_length=2, null=True, verbose_name='1'),
        ),
        migrations.AlterField(
            model_name='teethupperright',
            name='seven',
            field=models.CharField(blank=True, choices=[(None, '--'), ('KE', 'KE'), ('KD', 'KD'), ('KP', 'KP'), ('RG', 'RG'), ('AF', 'AF'), ('CF', 'CF'), ('GR', 'GR'), ('GP', 'GP'), ('PL', 'PL'), ('IM', 'IM'), ('In', 'In'), ('On', 'On'), ('Ab', 'Ab'), ('Cr', 'Cr'), ('Br', 'Br'), ('Ve', 'Ve'), ('M', 'M'), ('P', 'P')], default=None, max_length=2, null=True, verbose_name='7'),
        ),
        migrations.AlterField(
            model_name='teethupperright',
            name='six',
            field=models.CharField(blank=True, choices=[(None, '--'), ('KE', 'KE'), ('KD', 'KD'), ('KP', 'KP'), ('RG', 'RG'), ('AF', 'AF'), ('CF', 'CF'), ('GR', 'GR'), ('GP', 'GP'), ('PL', 'PL'), ('IM', 'IM'), ('In', 'In'), ('On', 'On'), ('Ab', 'Ab'), ('Cr', 'Cr'), ('Br', 'Br'), ('Ve', 'Ve'), ('M', 'M'), ('P', 'P')], default=None, max_length=2, null=True, verbose_name='6'),
        ),
        migrations.AlterField(
            model_name='teethupperright',
            name='three',
            field=models.CharField(blank=True, choices=[(None, '--'), ('KE', 'KE'), ('KD', 'KD'), ('KP', 'KP'), ('RG', 'RG'), ('AF', 'AF'), ('CF', 'CF'), ('GR', 'GR'), ('GP', 'GP'), ('PL', 'PL'), ('IM', 'IM'), ('In', 'In'), ('On', 'On'), ('Ab', 'Ab'), ('Cr', 'Cr'), ('Br', 'Br'), ('Ve', 'Ve'), ('M', 'M'), ('P', 'P')], default=None, max_length=2, null=True, verbose_name='3'),
        ),
        migrations.AlterField(
            model_name='teethupperright',
            name='two',
            field=models.CharField(blank=True, choices=[(None, '--'), ('KE', 'KE'), ('KD', 'KD'), ('KP', 'KP'), ('RG', 'RG'), ('AF', 'AF'), ('CF', 'CF'), ('GR', 'GR'), ('GP', 'GP'), ('PL', 'PL'), ('IM', 'IM'), ('In', 'In'), ('On', 'On'), ('Ab', 'Ab'), ('Cr', 'Cr'), ('Br', 'Br'), ('Ve', 'Ve'), ('M', 'M'), ('P', 'P')], default=None, max_length=2, null=True, verbose_name='2'),
        ),
        migrations.CreateModel(
            name='MedicalImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('patient', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='medical_image', to='patient.patients')),
            ],
            options={
                'db_table': 'medical_image',
            },
        ),
    ]
