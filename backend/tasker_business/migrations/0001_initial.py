# Generated by Django 2.2.16 on 2020-09-17 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('task_category', '0001_initial'),
        ('task_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timeslot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TaskerSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('rate', models.FloatField()),
                ('description', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taskerskill_category', to='task_category.Category')),
                ('subcategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='taskerskill_subcategory', to='task_category.Subcategory')),
                ('tasker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taskerskill_tasker', to='task_profile.TaskerProfile')),
            ],
        ),
        migrations.CreateModel(
            name='TaskerAvailability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tasker', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='taskeravailability_tasker', to='task_profile.TaskerProfile')),
                ('timeslots', models.ManyToManyField(related_name='taskeravailability_timeslots', to='tasker_business.Timeslot')),
            ],
        ),
        migrations.CreateModel(
            name='BusinessPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.URLField()),
                ('description', models.TextField()),
                ('tasker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='businessphoto_tasker', to='task_profile.TaskerProfile')),
            ],
        ),
    ]
