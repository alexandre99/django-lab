# Generated by Django 3.2.5 on 2021-07-17 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitaapp', '0003_receita_publicada'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='foto_receita',
            field=models.ImageField(blank=True, upload_to='fotos/%d/%m/%Y/'),
        ),
    ]
