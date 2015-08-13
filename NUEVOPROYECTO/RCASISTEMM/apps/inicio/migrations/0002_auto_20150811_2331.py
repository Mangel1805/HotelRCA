# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoCargo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Tipo', models.CharField(max_length=50)),
                ('Descripcion', models.CharField(max_length=140)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='perfiles',
            name='cargo',
            field=models.ForeignKey(blank=True, to='inicio.TipoCargo', null=True),
            preserve_default=True,
        ),
    ]
