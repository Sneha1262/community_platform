# Generated by Django 5.1.4 on 2024-12-08 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_edit_events'),
    ]

    operations = [
        migrations.CreateModel(
            name='delete_your_events',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
            ],
        ),
    ]
