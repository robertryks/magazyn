# Generated by Django 4.1.5 on 2023-01-12 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0002_add_grade'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeatModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Data aktualizacji')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Data utworzenia')),
                ('name', models.CharField(max_length=25, unique=True, verbose_name='Oznaczenie')),
            ],
            options={
                'verbose_name': 'Wytop',
                'verbose_name_plural': 'Wytopy',
                'db_table': 'heat',
                'ordering': ['name'],
            },
        ),
        migrations.AddIndex(
            model_name='heatmodel',
            index=models.Index(fields=['name'], name='heat_name_idx'),
        ),
    ]
