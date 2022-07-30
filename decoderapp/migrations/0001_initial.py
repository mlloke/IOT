# Generated by Django 3.1 on 2022-07-30 03:56

from django.db import migrations, models
import django.db.models.deletion
import jsoneditor.fields.django3_jsonfield


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dev_id', models.CharField(max_length=6, verbose_name='Device ID')),
            ],
        ),
        migrations.CreateModel(
            name='Decoder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schema_jsonfield', jsoneditor.fields.django3_jsonfield.JSONField(default=list)),
                ('start_date', models.DateTimeField(verbose_name='Start')),
                ('end_date', models.DateTimeField(verbose_name='End')),
                ('dev_id2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='decoderapp.devicelist')),
            ],
        ),
    ]