# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-31 15:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0023_alter_page_revision_on_delete_behaviour'),
        ('torchbox', '0027_marketinglandingpagerelatedlink_email_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarketingLandingPageFeaturedItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='featured_items', to='torchbox.MarketingLandingPage')),
                ('related_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.Page')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='marketinglandingpagerelatedlink',
            name='email_link',
            field=models.EmailField(blank=True, help_text="Enter email address only, without 'mailto:'", max_length=254, verbose_name='Email link'),
        ),
    ]
