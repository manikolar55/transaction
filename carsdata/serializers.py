from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.utils.serializer_helpers import ReturnDict

from .models import Block, CarsBlock, WishListCarsBlock, WishListBlock


class BookedSeatSerializer(serializers.Serializer):
    block = serializers.CharField(max_length=10, required=True)
    seat = serializers.IntegerField(required=True)
    booked = serializers.BooleanField(required=True)
    car_number = serializers.CharField(required=True)
    from_date_time = serializers.DateTimeField(required=True)
    end_date_time = serializers.DateTimeField(required=True)

    class Meta:
        model = CarsBlock
        fields = ["block", "seat"]

    def validate(self, attrs):
        block_data = Block.objects.filter(blocks=attrs["block"])
        if not block_data:
            raise ValidationError("Block does not exist")
        # data = CarsBlock.objects.filter(
        #     seat_number=attrs["seat"], block__blocks=attrs["block"]
        # ).first()
        # if data and data.taken:
        #     raise ValidationError("Seat already taken")
        return attrs

    @property
    def errors(self):
        """
        Returns custom error message

        Returns
        -------
        ReturnDict
            errors dict
        """
        x = super().errors
        if x:
            if x.get("non_field_errors"):
                return {"message": x["non_field_errors"][0], "success": False}
            elif x.get("block"):
                return {"message": "block field required", "success": False}
            elif x.get("booked"):
                return {"message": "booked field required", "success": False}
            elif x.get("seat"):
                return {"message": "seat field required", "success": False}
            elif x.get("car_number"):
                return {"message": "Car Number field required", "success": False}
            elif x.get("from_date_time"):
                return {"message": "Start Date Time field required", "success": False}
            elif x.get("to_date_time"):
                return {"message": "End Date Time field required", "success": False}
            return ReturnDict({"errors": x}, serializer=self)
        return ReturnDict(x, serializer=self)


class WishListBookedSeatSerializer(serializers.Serializer):
    block = serializers.CharField(max_length=10, required=True)
    seat = serializers.IntegerField(required=True)
    booked = serializers.BooleanField(required=True)
    car_number = serializers.CharField(required=True)
    from_date_time = serializers.DateTimeField(required=True)
    end_date_time = serializers.DateTimeField(required=True)
    class Meta:
        model = WishListCarsBlock
        fields = ["block", "seat"]

    def validate(self, attrs):
        block_data = WishListBlock.objects.filter(blocks=attrs["block"])
        if not block_data:
            raise ValidationError("Block does not exist")
        # data = CarsBlock.objects.filter(
        #     seat_number=attrs["seat"], block__blocks=attrs["block"]
        # ).first()
        # if data and data.taken:
        #     raise ValidationError("Seat already taken")
        return attrs

    @property
    def errors(self):
        """
        Returns custom error message

        Returns
        -------
        ReturnDict
            errors dict
        """
        x = super().errors
        if x:
            if x.get("non_field_errors"):
                return {"message": x["non_field_errors"][0], "success": False}
            elif x.get("block"):
                return {"message": "block field required", "success": False}
            elif x.get("booked"):
                return {"message": "booked field required", "success": False}
            elif x.get("seat"):
                return {"message": "seat field required", "success": False}
            elif x.get("car_number"):
                return {"message": "Car Number field required", "success": False}
            elif x.get("from_date_time"):
                return {"message": "Start Date Time field required", "success": False}
            elif x.get("end_date_time"):
                return {"message": "End Start Date Time field required", "success": False}
            return ReturnDict({"errors": x}, serializer=self)
        return ReturnDict(x, serializer=self)


class ChangeTimeSerializer(serializers.Serializer):
    from_date_time = serializers.DateTimeField(required=True)
    end_date_time = serializers.DateTimeField(required=True)

    @property
    def errors(self):
        """
        Returns custom error message

        Returns
        -------
        ReturnDict
            errors dict
        """
        x = super().errors
        if x:
            if x.get("non_field_errors"):
                return {"message": x["non_field_errors"][0], "success": False}
            elif x.get("from_date_time"):
                return {"message": "Start Date Time field required", "success": False}
            elif x.get("end_date_time"):
                return {"message": "End Start Date Time field required", "success": False}
            return ReturnDict({"errors": x}, serializer=self)
        return ReturnDict(x, serializer=self)
