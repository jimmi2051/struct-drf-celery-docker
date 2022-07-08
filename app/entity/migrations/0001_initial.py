# Generated by Django 4.0.5 on 2022-07-08 04:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='Updated At')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('isbn', models.CharField(max_length=13)),
            ],
            options={
                'db_table': 'book',
                'ordering': ['title'],
            },
        ),
    ]