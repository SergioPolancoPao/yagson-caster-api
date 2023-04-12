from django.db import models
from yagsoncasterapi.models import BaseModel

class Server(BaseModel):
    class Meta:
        db_table = 'servers'
    name = models.CharField(max_length=200)
    discord_id = models.IntegerField()
