# Generated by Django 4.1.1 on 2022-09-30 03:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turma', '0001_initial'),
        ('pessoa', '0004_remove_aluno_turma'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='turma',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='turma.turma'),
        ),
    ]