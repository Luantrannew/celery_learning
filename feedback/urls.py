from django.urls import path
from django.views.generic import RedirectView

from . import views

app_name = "feedback"

urlpatterns = [
    path('',RedirectView.as_view(url='feedback', permanent=False)),
    path('feedback/', views.feedback_form_view, name='feedback'),
    path('success/', views.success_view, name='success'),
]