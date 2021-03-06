# Generated by Django 2.0 on 2017-12-18 03:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('race_name', models.CharField(default='', max_length=20)),
                ('strength_modifier', models.IntegerField(default=0)),
                ('agility_modifier', models.IntegerField(default=0)),
                ('constitution_modifier', models.IntegerField(default=0)),
                ('intelligence_modifier', models.IntegerField(default=0)),
                ('wisdom_modifier', models.IntegerField(default=0)),
                ('charisma_modifier', models.IntegerField(default=0)),
                ('speed', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='RaceTrait',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trait_name', models.CharField(default='', max_length=50)),
                ('trait_effect', models.CharField(default='', max_length=1000)),
                ('race', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='character_builder.Race')),
            ],
        ),
        migrations.AddField(
            model_name='language',
            name='character',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='character_builder.Race'),
        ),
    ]
