# Generated by Django 2.2.10 on 2020-02-17 22:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('animals', '0002_auto_20200217_2154'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeighIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('weight', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animals.Animal')),
            ],
        ),
        migrations.CreateModel(
            name='Shed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('success', models.BooleanField()),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animals.Animal')),
            ],
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('measurement', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animals.Animal')),
            ],
        ),
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('feed', models.CharField(choices=[('PI', 'Pinky'), ('TP', 'Two Pinkies'), ('SF', 'Small Fuzzy'), ('RF', 'Regular Fuzzy'), ('HO', 'Hopper'), ('SA', 'Small Adult'), ('RA', 'Regular Adult'), ('LA', 'Large Adult')], default='PI', max_length=2)),
                ('feed_weight', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('success', models.BooleanField()),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animals.Animal')),
            ],
        ),
        migrations.CreateModel(
            name='DailyCheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('water_changed', models.BooleanField()),
                ('animal_seen', models.BooleanField()),
                ('temperature_measured', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animals.Animal')),
            ],
        ),
    ]