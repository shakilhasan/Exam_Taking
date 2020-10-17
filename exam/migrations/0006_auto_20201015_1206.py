# Generated by Django 2.2.16 on 2020-10-15 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0005_auto_20201014_1636'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='question',
            name='choice1',
        ),
        migrations.RemoveField(
            model_name='question',
            name='choice2',
        ),
        migrations.RemoveField(
            model_name='question',
            name='choice3',
        ),
        migrations.RemoveField(
            model_name='question',
            name='choice4',
        ),
        migrations.RemoveField(
            model_name='question',
            name='choice5',
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question', to='exam.Question'),
        ),
        migrations.AddField(
            model_name='choice',
            name='result',
            field=models.BooleanField(default=False),
        ),
    ]