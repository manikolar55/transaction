from django.db import models


# Create your models here.
class Block(models.Model):
    STATUS = (
        ("BlockA", ("A")),
        ("BlockB", ("B")),
        ("BlockC", ("C")),
    )
    blocks = models.CharField(max_length=10, choices=STATUS)

    def __str__(self):
        return self.blocks

    class Meta:
        db_table = "block"


class CarsBlock(models.Model):
    user = models.IntegerField(null=True, blank=True)
    block = models.ForeignKey(Block, on_delete=models.PROTECT)
    seat_number = models.IntegerField()
    taken = models.BooleanField(default=False)

    def __str__(self):
        return self.seat_number, self.user, self.block, self.taken

    class Meta:
        db_table = "cars_model"