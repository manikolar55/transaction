from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import BookingData, BookedSeat

urlpatterns = [
    path("booking/data", BookingData.as_view()),
    path("booking/seats", BookedSeat.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
