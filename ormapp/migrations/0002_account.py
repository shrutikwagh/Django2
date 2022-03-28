# Generated by Django 4.0 on 2022-01-20 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ormapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.IntegerField()),
                ('month', models.CharField(max_length=30)),
                ('year', models.IntegerField()),
                ('emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ormapp.emp')),
            ],
        ),
    ]