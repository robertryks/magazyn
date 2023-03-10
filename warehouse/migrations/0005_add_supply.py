# Generated by Django 4.1.5 on 2023-01-12 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0004_add_certificate'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupplyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Data aktualizacji')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Data utworzenia')),
                ('number', models.CharField(max_length=25, unique=True, verbose_name='Dokument')),
                ('date', models.DateField(verbose_name='Data')),
                ('can_modify', models.BooleanField(default=True, verbose_name='Modyfikacja')),
            ],
            options={
                'verbose_name': 'Przychód',
                'verbose_name_plural': 'Przychody',
                'db_table': 'supply',
                'ordering': ['number'],
                'get_latest_by': 'date',
            },
        ),
        migrations.AddIndex(
            model_name='supplymodel',
            index=models.Index(fields=['number'], name='supply_number_idx'),
        ),
        migrations.AddIndex(
            model_name='supplymodel',
            index=models.Index(fields=['date'], name='supply_date_idx'),
        ),
    ]
