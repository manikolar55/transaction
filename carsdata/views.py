from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED

from .models import CarsBlock, Block, WishListBlock, WishListCarsBlock
from .serializers import BookedSeatSerializer, WishListBookedSeatSerializer, ChangeTimeSerializer


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
                my_dict[block.seat_number] = {"seat_booked": block.taken, "car_number:": block.car_number,
                                              "from_date_time":block.date_time, "to_date_time": block.date_time_drop}
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
                car_data.date_time = data["from_date_time"]
                car_data.date_time_drop = data["end_date_time"]
                car_data.user = request.user.id
                car_data.save(update_fields=["taken", "user", "car_number", "date_time", "date_time_drop"])
                return Response("Seat Booked", status=HTTP_201_CREATED)
            else:
                car_data.taken = data["booked"]
                car_data.car_number = None
                car_data.user = request.user.id
                car_data.date_time = None
                car_data.save(update_fields=["taken", "user", "car_number", "date_time"])
                return Response("Seat Dropped", status=HTTP_201_CREATED)
        else:
            return Response("Data Not Found", status=HTTP_201_CREATED)


class WishListBookingData(APIView):
    def get(self, request):

        response_list = []
        final_dict = {}
        cars_block = WishListBlock.objects.all()
        for data in cars_block:
            count = 0
            booked_list = []
            my_dict = {}
            cars_data = WishListCarsBlock.objects.filter(block__blocks=data.blocks)
            for block in cars_data:
                # cound_data = "car_number {}".format(count)
                my_dict[block.seat_number] = {"seat_booked": block.taken, "car_number:": block.car_number,
                                              "from_date_time":block.date_time, "to_date_time": block.date_time_drop}
                # my_dict[cound_data] = block.car_number
                # count += 1
            final_dict[data.blocks] = my_dict

        res = {"data": [final_dict]}
        return Response(res, status=HTTP_200_OK)


class WishListBookedSeat(APIView):
    def post(self, request):
        data = request.data
        serializer = WishListBookedSeatSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        car_data = WishListCarsBlock.objects.filter(
            block__blocks=data["block"], seat_number=data["seat"]
        ).first()
        if car_data:
            if data["booked"] == "True":
                car_data.taken = data["booked"]
                car_data.car_number = data["car_number"]
                car_data.date_time = data["from_date_time"]
                car_data.date_time_drop = data["end_date_time"]
                car_data.user = request.user.id
                car_data.save(update_fields=["taken", "user", "car_number", "date_time", "date_time_drop"])
                return Response("Seat Booked", status=HTTP_201_CREATED)
            else:
                car_data.taken = data["booked"]
                car_data.car_number = None
                car_data.user = request.user.id
                car_data.date_time = None
                car_data.save(update_fields=["taken", "user", "car_number", "date_time"])
                return Response("Seat Dropped", status=HTTP_201_CREATED)
        else:
            return Response("Data Not Found", status=HTTP_201_CREATED)


class DropCarGet(APIView):
    def get(self, request):

        response_list = []
        final_dict = {}
        user_id = request.user.id
        cars_block = WishListBlock.objects.all()
        for data in cars_block:
            count = 0
            booked_list = []
            my_dict = {}
            cars_data = WishListCarsBlock.objects.filter(block__blocks=data.blocks, user=user_id)
            for block in cars_data:
                # cound_data = "car_number {}".format(count)
                my_dict[block.seat_number] = {"id": block.id, "seat_booked": block.taken, "car_number:": block.car_number,
                                              "from_date_time":block.date_time, "to_date_time": block.date_time_drop}
                # my_dict[cound_data] = block.car_number
                # count += 1
            final_dict[data.blocks] = my_dict

        res = {"data": [final_dict]}
        return Response(res, status=HTTP_200_OK)


class CarDropPost(APIView):
    def post(self, request):
        data = request.data
        data_id = data["id"]
        user_id = request.user.id
        cars_data = WishListCarsBlock.objects.filter(id=data_id, user=user_id).first()
        if cars_data:
            cars_data.taken = False
            cars_data.car_number = None
            cars_data.user = None
            cars_data.date_time = None
            cars_data.save(update_fields=["taken", "user", "car_number", "date_time"])
            return Response("Seat Dropped", status=HTTP_201_CREATED)



class ChangeTime(APIView):
    def get(self, request):

        response_list = []
        final_dict = {}
        user_id = request.user.id
        cars_block = WishListBlock.objects.all()
        for data in cars_block:
            count = 0
            booked_list = []
            my_dict = {}
            cars_data = WishListCarsBlock.objects.filter(block__blocks=data.blocks, user=user_id)
            for block in cars_data:
                # cound_data = "car_number {}".format(count)
                my_dict[block.seat_number] = {"id": block.id, "seat_booked": block.taken, "car_number:": block.car_number,
                                              "from_date_time":block.date_time, "to_date_time": block.date_time_drop}
                # my_dict[cound_data] = block.car_number
                # count += 1
            final_dict[data.blocks] = my_dict

        res = {"data": [final_dict]}
        return Response(res, status=HTTP_200_OK)


class ChangeTimePost(APIView):
    def post(self, request):
        data = request.data
        serializer = ChangeTimeSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        data_id = data["id"]
        date_time = data["from_date_time"]
        end_date_time = data["end_date_time"]
        user_id = request.user.id
        cars_data = WishListCarsBlock.objects.filter(id=data_id, user=user_id).first()
        if cars_data:
            cars_data.date_time = date_time
            cars_data.date_time_drop = end_date_time
            cars_data.save(update_fields=["date_time", "date_time_drop"])
            return Response("Time Updated", status=HTTP_201_CREATED)
