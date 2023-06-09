from django.urls import path, include
from rest_framework import routers, serializers, viewsets
import sentry_sdk

def trigger_error(request):
    division_by_zero = 1 / 0

@sentry_sdk.configure_scope
def trigger_error_2(request):
    with sentry_sdk.start_span(op='test_operation', description='Test Operation'):
        division_by_zero = 1 / 0

from .views import InventoreyView, HandledErrorView, UnHandledErrorView, CaptureMessageView


urlpatterns = [
    path('checkout', InventoreyView.as_view()),
    path('handled', HandledErrorView.as_view()),
    path('unhandled', UnHandledErrorView.as_view()),
    path('message', CaptureMessageView.as_view()),
    path('sentry-debug/', trigger_error),
    path('sentry-debug-2/', trigger_error_2),

]
