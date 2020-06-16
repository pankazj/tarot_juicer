# Generated by Django 2.2.13 on 2020-06-16 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('essays', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Generator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=24)),
                ('number', models.IntegerField()),
                ('tarot_card_image', models.CharField(max_length=1024)),
                ('tarot_card_thumbnail', models.ImageField(upload_to='thumbnails/')),
                ('astrological', models.CharField(max_length=140)),
                ('alchemical', models.CharField(max_length=140)),
                ('intelligence', models.CharField(max_length=140)),
                ('hebrew_letter', models.CharField(max_length=140)),
                ('letter_meaning', models.CharField(max_length=140)),
                ('watchtower_position', models.IntegerField(blank=True, null=True)),
                ('slashdot_position', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True)),
                ('description_bullets', models.TextField(help_text='Please use line space for bullet points', null=True)),
                ('galileo_content', models.TextField(blank=True)),
                ('galileo_bullets', models.TextField(blank=True, help_text='Please use line space for bullet points')),
                ('f_loss_content', models.TextField(blank=True)),
                ('f_loss_bullets', models.TextField(blank=True, help_text='Please use line space for bullet points')),
                ('st_paul_content', models.TextField(blank=True)),
                ('st_paul_bullets', models.TextField(blank=True, help_text='Please use line space for bullet points')),
                ('biblio', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bibliography', to='essays.BibliographyArticle')),
                ('content_changes_logged', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='content_changes', to='essays.ContentChanges')),
            ],
        ),
    ]