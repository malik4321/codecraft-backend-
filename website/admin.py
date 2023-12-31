from django.contrib import admin
from . models  import User, TableSubmission, Question, Ranking,Project


# Register your models here.

admin.site.register(User)
admin.site.register(TableSubmission)
admin.site.register(Question)
admin.site.register(Ranking)
admin.site.register(Project)