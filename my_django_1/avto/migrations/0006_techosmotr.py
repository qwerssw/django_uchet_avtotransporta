# Generated by Django 4.2 on 2023-04-18 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('avto', '0005_strahovki'),
    ]

    operations = [
        migrations.CreateModel(
            name='Techosmotr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zakazchik', models.CharField(max_length=15, verbose_name='zakazchik')),
                ('data_vydachi', models.DateField(verbose_name='data_vydachi')),
                ('srok_deistviya', models.DateField(verbose_name='srok_deistviya')),
                ('number_tex_karty', models.CharField(max_length=15, verbose_name='number_tex_karty')),
                ('cars', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='avto.cars')),
            ],
            options={
                'verbose_name': 'Техосмотр',
                'verbose_name_plural': 'Техосмотры',
            },
        ),
    ]
