# Generated by Django 3.2.3 on 2021-08-15 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smulithackathon', '0004_rename_businesstype_individual_indivtype'),
    ]

    operations = [
        migrations.AddField(
            model_name='individual',
            name='children',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
