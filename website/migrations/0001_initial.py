# Generated by Django 4.2.7 on 2023-12-16 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('QNo', models.AutoField(primary_key=True, serialize=False)),
                ('Type', models.CharField(max_length=50)),
                ('Difficulty', models.CharField(max_length=50)),
                ('Title', models.CharField(max_length=200)),
                ('Points', models.IntegerField()),
                ('Statement', models.TextField()),
                ('InputFormat', models.TextField()),
                ('OutputFormat', models.TextField()),
                ('InputConstraint', models.TextField()),
                ('SampleData', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('UserId', models.AutoField(primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=100)),
                ('LastName', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TableSubmission',
            fields=[
                ('SubmitId', models.AutoField(primary_key=True, serialize=False)),
                ('IsSuccessful', models.BooleanField()),
                ('SubmitLang', models.CharField(max_length=50)),
                ('CreatedAt', models.DateTimeField()),
                ('CreatorId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.user')),
                ('QNumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.question')),
            ],
        ),
        migrations.CreateModel(
            name='Ranking',
            fields=[
                ('RankId', models.AutoField(primary_key=True, serialize=False)),
                ('Lang', models.CharField(max_length=50)),
                ('Points', models.IntegerField()),
                ('Level', models.IntegerField()),
                ('UserId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.user')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('ProjectId', models.AutoField(primary_key=True, serialize=False)),
                ('ProjName', models.CharField(max_length=200)),
                ('DateModified', models.DateField()),
                ('ProjectContent', models.TextField()),
                ('IsTrash', models.BooleanField()),
                ('IsArchived', models.BooleanField()),
                ('OwnerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.user')),
            ],
        ),
    ]
