# Generated by Django 3.1.3 on 2021-04-30 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0003_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='Todoitems',
            new_name='todoitem',
        ),
    ]
