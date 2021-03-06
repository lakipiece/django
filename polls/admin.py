from django.contrib import admin
from polls.models import Question, Choice

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    fieldsets = [
        ('Question Statement', {'fields':['question_text']}),
        ('Date Information', {'fields':['pub_date'], 'classes':['collapse']})
    ]

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)

