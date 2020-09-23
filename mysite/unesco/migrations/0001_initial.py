# Generated by Django 3.0.9 on 2020-09-23 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Iso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('year', models.IntegerField(null=True)),
                ('area_hectares', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('latitude', models.FloatField(null=True)),
                ('justification', models.TextField()),
                ('description', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unesco.Category')),
                ('iso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unesco.Iso')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unesco.Region')),
                ('states', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unesco.States')),
            ],
        ),
    ]
