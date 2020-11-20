# Generated by Django 3.0.8 on 2020-11-07 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctors', '0003_auto_20201107_1856'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=30)),
                ('symptoms', models.CharField(max_length=80)),
                ('diagnosis', models.CharField(max_length=30)),
                ('received_at', models.DateTimeField(auto_now=True)),
                ('signed_out', models.BooleanField(default=False)),
                ('room_number', models.PositiveIntegerField()),
                ('doctor_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctors.Doctors')),
            ],
        ),
    ]