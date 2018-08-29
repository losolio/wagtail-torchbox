# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-08-29 14:41
from __future__ import unicode_literals

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('torchbox', '0099_auto_20180320_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicepage',
            name='streamfield',
            field=wagtail.core.fields.StreamField([('case_studies', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('intro', wagtail.core.blocks.TextBlock(required=True)), ('case_studies', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('page', wagtail.core.blocks.PageChooserBlock('torchbox.WorkPage')), ('title', wagtail.core.blocks.CharBlock(required=False)), ('descriptive_title', wagtail.core.blocks.CharBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))])))])), ('highlights', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('intro', wagtail.core.blocks.RichTextBlock(required=False)), ('highlights', wagtail.core.blocks.ListBlock(wagtail.core.blocks.TextBlock()))])), ('pull_quote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.CharBlock(classname='quote title')), ('attribution', wagtail.core.blocks.CharBlock())], template='blocks/pull_quote_block.html')), ('process', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('intro', wagtail.core.blocks.TextBlock(required=False)), ('steps', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('subtitle', wagtail.core.blocks.CharBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(required=True)), ('icon', wagtail.core.blocks.CharBlock(help_text='Paste SVG code here', max_length=9000, required=True)), ('description', wagtail.core.blocks.RichTextBlock(required=True))])))])), ('people', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('intro', wagtail.core.blocks.RichTextBlock(required=True)), ('people', wagtail.core.blocks.ListBlock(wagtail.core.blocks.PageChooserBlock()))])), ('featured_pages', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('pages', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('page', wagtail.core.blocks.PageChooserBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.core.blocks.TextBlock()), ('sub_text', wagtail.core.blocks.CharBlock(max_length=100))])))])), ('sign_up_form_page', wagtail.core.blocks.StructBlock([('page', wagtail.core.blocks.PageChooserBlock('torchbox.SignUpFormPage'))])), ('logos', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('intro', wagtail.core.blocks.CharBlock()), ('logos', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('link_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('link_external', wagtail.core.blocks.URLBlock(required=False))])))]))]),
        ),
    ]
