# Generated by Django 3.1.7 on 2021-06-07 01:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ebigay', '0004_ayudaapplicant_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='CityChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ebigay.city')),
            ],
        ),
        migrations.CreateModel(
            name='AyudaDropoff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ayudaapplicant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ebigay.ayudaapplicant')),
            ],
        ),
    ]
