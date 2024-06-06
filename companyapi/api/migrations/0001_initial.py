# Generated by Django 5.0.1 on 2024-05-28 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('comp_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('localtion', models.CharField(max_length=100)),
                ('about', models.TextField()),
                ('types', models.CharField(choices=[('IT', 'IT'), ('Non IT', 'Non IT'), ('Mobiles', 'Mobiles')], max_length=100)),
                ('added_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
