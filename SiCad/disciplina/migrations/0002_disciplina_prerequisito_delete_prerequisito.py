# Generated by Django 4.1.1 on 2022-10-26 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disciplina', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='disciplina',
            name='preRequisito',
            field=models.ManyToManyField(blank=True, null=True, to='disciplina.disciplina', verbose_name='preRequisito'),
        ),
        migrations.DeleteModel(
            name='PreRequisito',
        ),
    ]
