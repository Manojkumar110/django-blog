from django.contrib import admin
from djangopolls.models import Question, Choice
# Register your models here.


class ChoiceModelAdmin(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionModelAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]

    list_display = ['pub_date', 'question_text',]
    list_filter = ['pub_date']
    inlines = [ChoiceModelAdmin]

admin.site.register(Question, QuestionModelAdmin),

