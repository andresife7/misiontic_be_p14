# Generated by Django 3.2.7 on 2021-11-09 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servicioCliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PQR',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=32)),
                ('info', models.TextField()),
                ('created', models.DateField()),
                ('soporte', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='servicioCliente.soporte')),
            ],
        ),
    ]
