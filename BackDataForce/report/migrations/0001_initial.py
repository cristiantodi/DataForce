# Generated by Django 4.2.6 on 2023-11-03 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniqueCode', models.CharField(blank=True, max_length=200, null=True)),
                ('generationDate', models.DateTimeField(auto_now_add=True)),
                ('uniqueReportIdentifier', models.CharField(blank=True, max_length=200, null=True)),
                ('ReportDate', models.DateField(blank=True, null=True)),
                ('architecture', models.IntegerField(blank=True, null=True)),
                ('platform', models.IntegerField(blank=True, null=True)),
                ('uniqueDeviceId', models.CharField(blank=True, max_length=200, null=True)),
                ('productName', models.CharField(blank=True, max_length=200, null=True)),
                ('maker', models.CharField(blank=True, max_length=200, null=True)),
                ('model', models.CharField(blank=True, max_length=200, null=True)),
                ('productCode', models.CharField(blank=True, max_length=200, null=True)),
                ('serial_so', models.CharField(blank=True, max_length=200, null=True)),
                ('code_so', models.CharField(blank=True, max_length=200, null=True)),
                ('model_id', models.CharField(blank=True, max_length=200, null=True)),
                ('computerMD', models.CharField(blank=True, max_length=200, null=True)),
                ('conputerSHA', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
