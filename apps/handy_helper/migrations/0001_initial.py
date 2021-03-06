# Generated by Django 2.1.1 on 2018-09-24 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=128)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='login_registration.User')),
                ('workers', models.ManyToManyField(related_name='workers', to='login_registration.User')),
            ],
        ),
    ]
