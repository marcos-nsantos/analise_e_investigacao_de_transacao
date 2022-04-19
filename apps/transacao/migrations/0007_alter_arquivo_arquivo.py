# Generated by Django 3.2.13 on 2022-04-15 10:28

from django.db import migrations, models
import transacao.validators.csv_file


class Migration(migrations.Migration):

    dependencies = [
        ('transacao', '0006_auto_20220412_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arquivo',
            name='arquivo',
            field=models.FileField(default='', upload_to='arquivos_csv/', validators=[transacao.validators.csv_file.is_csv_file, transacao.validators.csv_file.is_file_empty], verbose_name='Arquivo'),
            preserve_default=False,
        ),
    ]
