# Generated by Django 2.2.16 on 2020-10-14 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0003_submission_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer1', to='exam.Choice'),
        ),
    ]