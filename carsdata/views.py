from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED

from .models import CarsBlock, Block
from .serializers import BookedSeatSerializer

# Create your views here.


class BookingData(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):

        response_list = []
        cars_block = Block.objects.all()
        for data in cars_block:
            booked_list = []
            cars_data = CarsBlock.objects.filter(block__blocks=data.blocks)
            taken_seats = cars_data.filter(taken=True)
            for seats in taken_seats:
                booked_list.append(seats.seat_number)

            res = {
                data.blocks: {
                    "total_seats": len(cars_data),
                    "booked_seats": booked_list,
                }
            }
            response_list.append(res)

        response = {"data": response_list}
        return Response(response, status=HTTP_200_OK)


class BookedSeat(APIView):
    def post(self, request):
        data = request.data
        serializer = BookedSeatSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        car_data = CarsBlock.objects.filter(block__blocks=data["block"], seat_number=data["seat"]).first()
        if car_data:
            car_data.taken = data["booked"]
            car_data.user = request.user.id
            car_data.save(update_fields=["taken", "user"])
            return Response("seat booked", status=HTTP_201_CREATED)
        else:
            return Response("Data Not Found", status=HTTP_201_CREATED)
