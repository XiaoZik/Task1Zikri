# Generated by Django 4.0.6 on 2022-07-29 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('text', models.CharField(max_length=2000)),
                ('attachment', models.CharField(max_length=2000)),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
