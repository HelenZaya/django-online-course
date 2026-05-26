from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Course, Enrollment, Question, Choice, Submission


def index(request):
    courses = Course.objects.all()
    return render(request, 'onlinecourse/index.html', {'courses': courses})


def enroll(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    user = request.user
    if not Enrollment.objects.filter(user=user, course=course).exists():
        Enrollment.objects.create(user=user, course=course, mode='honor')
        course.total_enrollment += 1
        course.save()
    return HttpResponseRedirect(reverse('onlinecourse:course_details', args=(course.id,)))


def course_details(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'onlinecourse/course_details_bootstrap.html', {'course': course})


def submit(request, course_id):
    user = request.user
    course = get_object_or_404(Course, pk=course_id)
    enrollment = get_object_or_404(Enrollment, user=user, course=course)
    submission = Submission(enrollment=enrollment)
    submission.save()
    for key, value in request.POST.items():
        if key.startswith('choice'):
            try:
                selected_choice = Choice.objects.get(pk=int(value))
                submission.choices.add(selected_choice)
                submission.save()
            except Choice.DoesNotExist:
                pass
    return HttpResponseRedirect(
        reverse('onlinecourse:show_exam_result', args=(course.id, submission.id))
    )


def show_exam_result(request, course_id, submission_id):
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)
    choices = submission.choices.all()
    selected_ids = choices.values_list('id', flat=True)
    total_score = 0
    for question in course.question_set.all():
        if question.is_get_score(selected_ids):
            total_score += question.grade
    return render(request, 'onlinecourse/exam_result.html', {
        'course': course,
        'submission': submission,
        'total_score': total_score,
    })
