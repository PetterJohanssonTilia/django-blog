# Generated by Django 4.2.1 on 2024-07-06 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_remove_comment_challenge"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="updated_on",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
