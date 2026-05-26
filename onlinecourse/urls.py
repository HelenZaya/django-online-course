from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'onlinecourse'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:course_id>/', views.course_details, name='course_details'),
    path('<int:course_id>/enroll/', views.enroll, name='enroll'),
    path('<int:course_id>/submit/', views.submit, name='submit'),
    path('<int:course_id>/submission/<int:submission_id>/result/',
         views.show_exam_result, name='exam_result'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
