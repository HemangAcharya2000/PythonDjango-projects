# Generated by Django 3.2.3 on 2021-06-08 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('gender', models.BooleanField()),
                ('fees', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.BooleanField(),
        ),
    ]
