# Generated by Django 4.0 on 2022-01-20 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('email', models.EmailField(max_length=30, null=True)),
                ('contact', models.CharField(max_length=15, null=True)),
                ('age', models.IntegerField(default=0)),
                ('address', models.TextField(max_length=300, null=True)),
            ],
        ),
    ]
