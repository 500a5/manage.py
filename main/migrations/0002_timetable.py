# Generated by Django 3.0.11 on 2021-02-08 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Day', models.CharField(max_length=50, verbose_name='День')),
                ('text', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timetable', to='main.Text', verbose_name='Расписание')),
            ],
            options={
                'verbose_name': 'Расписание',
                'verbose_name_plural': 'Расписание',
            },
        ),
    ]
