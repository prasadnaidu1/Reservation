# Generated by Django 2.1.1 on 2018-10-31 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('c_no', models.IntegerField(default=10, primary_key=True, serialize=False)),
                ('cvv', models.IntegerField(default=3)),
                ('amount', models.IntegerField(default=10)),
                ('des', models.CharField(max_length=100)),
            ],
        ),
    ]