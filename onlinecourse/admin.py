from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner, Enrollment, Question, Choice


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 4


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 5


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


class LessonAdmin(admin.ModelAdmin):
    pass


class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline, QuestionInline]


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Enrollment)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
