from django.contrib import admin
from djangopolls.models import Question, Choice
# Register your models here.


class ChoiceModelAdmin(admin.TabularInline):
    model = Choice
    extra = 4
class QuestionModelAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     (None, {"fields": ["question_text","slug"]}),
    #     ("Date information", {"fields": ["pub_date"]}),
    # ]
    
    prepopulated_fields = {"slug": ("question_text",)}
    list_display = ['pub_date', 'question_text',]
    list_filter = ['pub_date']
    inlines = [ChoiceModelAdmin]

admin.site.register(Question, QuestionModelAdmin),

