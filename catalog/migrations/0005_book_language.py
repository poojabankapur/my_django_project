# Generated by Django 3.1.1 on 2020-09-10 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20200908_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.language'),
        ),
    ]
