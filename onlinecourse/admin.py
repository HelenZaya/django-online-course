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
    list_display = ['content', 'course', 'grade']


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'order']


class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline, QuestionInline]
    list_display = ['name', 'pub_date', 'total_enrollment']


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Enrollment)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
