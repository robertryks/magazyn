# Generated by Django 4.1.5 on 2023-01-07 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GradeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Data aktualizacji')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Data utworzenia')),
                ('name', models.CharField(error_messages={'unique': 'Taki gatunek już istnieje w bazie danych.'}, max_length=25, unique=True, verbose_name='Oznaczenie')),
            ],
            options={
                'verbose_name': 'Gatunek',
                'verbose_name_plural': 'Gatunki',
                'db_table': 'grade',
                'ordering': ['name'],
            },
        ),
        migrations.AddIndex(
            model_name='grademodel',
            index=models.Index(fields=['name'], name='grade_name_idx'),
        ),
    ]
