# Generated by Django 4.2.2 on 2023-06-11 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0003_modalform'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormModal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=30, verbose_name='Имя клиента')),
                ('phone', models.CharField(max_length=30, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
    ]
