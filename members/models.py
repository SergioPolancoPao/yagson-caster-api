from django.db import models
from yagsoncasterapi.models import BaseModel
from servers.models import Server

class Member(BaseModel):
    class Meta:
        db_table = 'members'
    name = models.CharField(max_length=200)
    server = models.ManyToManyField(Server)
    discord_id = models.IntegerField()