# Generated by Django 3.2.13 on 2022-04-22 19:52

from django.db import migrations, models
import transacao.validators.csv_validator


class Migration(migrations.Migration):

    dependencies = [
        ('transacao', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arquivo',
            name='arquivo',
            field=models.FileField(upload_to='csv_files/', validators=[transacao.validators.csv_validator.validate_csv], verbose_name='Arquivo'),
        ),
    ]
