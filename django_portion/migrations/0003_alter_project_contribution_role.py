# Generated by Django 5.0.4 on 2024-04-25 16:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "django_portion",
            "0002_resume_skill_post_comment_project_projectimage_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="contribution_role",
            field=models.TextField(blank=True, help_text="Your role in the project"),
        ),
    ]
