from django.db import models


class MCServer(models.Model):
    server_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)
    description = models.TextField()
    client_json_url = models.URLField()
    client_json_size = models.BigIntegerField()
    modded = models.BooleanField()

    class Meta:
        db_table = "mc_server"


class MCModPack(models.Model):
    modpack_id = models.IntegerField(primary_key=True)
    server = models.ForeignKey(MCServer, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    description = models.TextField()
    required = models.BooleanField()
    url = models.URLField()
    size = models.BigIntegerField()

    class Meta:
        db_table = "mc_modpack"
