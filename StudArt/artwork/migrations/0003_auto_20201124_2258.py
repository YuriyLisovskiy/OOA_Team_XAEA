# Generated by Django 3.1.2 on 2020-11-24 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0002_auto_20201124_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentmodel',
            name='artwork',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='artwork.artworkmodel'),
        ),
        migrations.AlterField(
            model_name='commentmodel',
            name='comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='artwork.commentmodel'),
        ),
    ]
