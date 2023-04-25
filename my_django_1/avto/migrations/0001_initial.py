# Generated by Django 4.2 on 2023-04-17 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Voditels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=50, verbose_name='fio')),
                ('number_prav', models.CharField(max_length=15, verbose_name='number_prav')),
                ('conec_prav', models.DateField(verbose_name='conec_prav')),
                ('number_avto', models.CharField(max_length=15, verbose_name='number_avto')),
                ('primechanie', models.TextField(verbose_name='primechanie')),
            ],
            options={
                'verbose_name': 'Водитель',
                'verbose_name_plural': 'Водители',
            },
        ),
    ]
