# Generated by Django 3.1.3 on 2021-04-30 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0002_remove_todoitem_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('avatar', models.CharField(max_length=255)),
                ('Todoitems', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp1.todoitem')),
            ],
        ),
    ]
