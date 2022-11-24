from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Block, CarsBlock


class BookedSeatSerializer(serializers.Serializer):
    block = serializers.CharField(max_length=10, required=True)
    seat = serializers.IntegerField(required=True)

    class Meta:
        model = CarsBlock
        fields = ["block", "seat"]

    def validate(self, attrs):
        block_data = Block.objects.filter(blocks=attrs["block"])
        if not block_data:
            raise ValidationError("Block does not exist")
        data = CarsBlock.objects.filter(seat_number=attrs["seat"], block__blocks=attrs["block"]).first()
        if data and data.taken:
            raise ValidationError("Seat already taken")
        return block_data
