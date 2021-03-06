# Generated by Django 4.0.2 on 2022-02-18 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='categoria',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='marca',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='modelo',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='sku',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='sub_categoria',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='fabricante',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
