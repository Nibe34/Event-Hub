# Generated by Django 5.1.6 on 2025-02-27 01:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Очікується'), ('confirmed', 'Підтверджено'), ('canceled', 'Скасовано')], default='pending', max_length=10)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registrations', to='events.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registrations', to='users.user')),
            ],
            options={
                'unique_together': {('user', 'event')},
            },
        ),
    ]
