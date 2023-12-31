from django.contrib import admin
from djangopolls.models import Question, Choice
# Register your models here.


class ChoiceModelAdmin(admin.TabularInline):
    model = Choice
    extra = 4
class QuestionModelAdmin(admin.ModelAdmin):
    
    prepopulated_fields = {"slug": ("question_text",)}
    list_display = ['pub_date', 'question_text',]
    list_filter = ['pub_date']
    search_fields = ['question_text']
    inlines = [ChoiceModelAdmin]

admin.site.register(Question, QuestionModelAdmin),

