from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED

from .models import CarsBlock, Block
from .serializers import BookedSeatSerializer

# Create your views here.


class BookingData(APIView):

    def get(self, request):

        response_list = []
        final_dict = {}
        cars_block = Block.objects.all()
        for data in cars_block:
            count = 0
            booked_list = []
            my_dict = {}
            cars_data = CarsBlock.objects.filter(block__blocks=data.blocks)
            for block in cars_data:
                # cound_data = "car_number {}".format(count)
                my_dict[block.seat_number] = [block.taken, block.car_number]
                # my_dict[cound_data] = block.car_number
                # count += 1
            final_dict[data.blocks] = my_dict

        res = {"data": [final_dict]}
        return Response(res, status=HTTP_200_OK)


class BookedSeat(APIView):
    def post(self, request):
        data = request.data
        serializer = BookedSeatSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        car_data = CarsBlock.objects.filter(
            block__blocks=data["block"], seat_number=data["seat"]
        ).first()
        if car_data:
            if data["booked"] == "True":
                car_data.taken = data["booked"]
                car_data.car_number = data["car_number"]
                car_data.user = request.user.id
                car_data.save(update_fields=["taken", "user", "car_number"])
                return Response("Seat Booked", status=HTTP_201_CREATED)
            else:
                car_data.taken = data["booked"]
                car_data.car_number = None
                car_data.user = request.user.id
                car_data.save(update_fields=["taken", "user", "car_number"])
                return Response("Seat Dropped", status=HTTP_201_CREATED)
        else:
            return Response("Data Not Found", status=HTTP_201_CREATED)
