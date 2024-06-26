# Generated by Django 4.2.6 on 2024-05-21 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CUR_UNIT', models.CharField(max_length=100)),
                ('CUR_NM', models.CharField(max_length=100)),
                ('TTB', models.CharField(max_length=100)),
                ('TTS', models.CharField(max_length=100)),
                ('DEAL_BAS_R', models.CharField(max_length=100)),
                ('BKPR', models.CharField(max_length=100)),
                ('YY_EFEE_R', models.CharField(max_length=100)),
                ('TEN_DD_EFEE_R', models.CharField(max_length=100)),
                ('kor_to_cur', models.FloatField()),
            ],
        ),
    ]
