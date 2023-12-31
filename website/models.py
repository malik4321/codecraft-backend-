from django.db import models

# Create your models here.
# myapp/models.py
from django.db import models
import json

class User(models.Model):
    UserId = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Email = models.EmailField()
    Password = models.CharField(max_length=100)

class TableSubmission(models.Model):
    SubmitId = models.AutoField(primary_key=True)
    QNumber = models.ForeignKey('Question', on_delete=models.CASCADE)
    CreatorId = models.ForeignKey(User, on_delete=models.CASCADE)
    IsSuccessful = models.BooleanField()
    SubmitLang = models.CharField(max_length=50)
    CreatedAt = models.DateTimeField()

class Question(models.Model):
    QNo = models.AutoField(primary_key=True)
    Type = models.CharField(max_length=50)
    Difficulty = models.CharField(max_length=50)
    Title = models.CharField(max_length=200)
    Points = models.IntegerField()
    Statement = models.TextField()
    InputFormat = models.TextField()
    OutputFormat = models.TextField()
    InputConstraint = models.TextField()

    # Change SampleData to a JSONField
    SampleData = models.JSONField()

    def set_sample_data(self, data):
        self.SampleData = json.dumps(data)

    def get_sample_data(self):
        return json.loads(self.SampleData)

class Ranking(models.Model):
    RankId = models.AutoField(primary_key=True)
    UserId = models.ForeignKey(User, on_delete=models.CASCADE)
    Lang = models.CharField(max_length=50)
    Points = models.IntegerField()
    Level = models.IntegerField()

class Project(models.Model):
    ProjectId = models.AutoField(primary_key=True)
    ProjName = models.CharField(max_length=200)
    DateModified = models.DateField()
    ProjectContent = models.TextField()
    IsTrash = models.BooleanField()
    IsArchived = models.BooleanField()
    OwnerId = models.ForeignKey(User, on_delete=models.CASCADE)
