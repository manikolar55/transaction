from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import BookingData, BookedSeat, WishListBookingData, WishListBookedSeat, DropCarGet, CarDropPost, \
    ChangeTimePost, ChangeTime

urlpatterns = [
    path("booking/data", BookingData.as_view()),
    path("booking/seats", BookedSeat.as_view()),
    path("wish_list_booking/data", WishListBookingData.as_view()),
    path("wish_list_booking/seats", WishListBookedSeat.as_view()),
    path("dropcar", DropCarGet.as_view()),
    path("dropcarpost", CarDropPost.as_view()),
    path("changetime", ChangeTime.as_view()),
    path("changetimepost", ChangeTimePost.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
