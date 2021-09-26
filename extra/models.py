from django.db import models

from utils.db.fields import TinyAutoField


class TinyFieldModel(models.Model):
    """
    to demonstrate the usage of `TinyAutoField`.

    Since the `TinyAutoField` returning the `tinyint` type, the maximum value
    that can be hold is upto 255(for unsigned) and upto 127(for signed)

    See this: https://stackoverflow.com/questions/2991405/
    """

    id = TinyAutoField(primary_key=True)
    any_number = models.IntegerField(default=10)

    def __str__(self):
        return f"{self.id} -- {self.any_number}"
