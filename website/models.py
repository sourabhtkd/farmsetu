from django.db import models

# Create your models here.
from farmsetu.core_lib import CoreUtils
from django.core.validators import MinLengthValidator, MaxLengthValidator


class Climate(models.Model):
    id = models.CharField(max_length=24, primary_key=True, db_index=True, default=CoreUtils.get_bson_object_id)
    year = models.PositiveIntegerField(default=0, validators=[MinLengthValidator(4), MaxLengthValidator(4)])

