from django.db import models


class MCServer(models.Model):
    server_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)
    description = models.TextField()
    client_json_file_id = models.URLField()
    modded = models.BooleanField()

    class Meta:
        db_table = "mc_server"


class MCModPack(models.Model):
    modpack_id = models.IntegerField(primary_key=True)
    server = models.ForeignKey(MCServer, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    description = models.TextField()
    required = models.BooleanField()
    file_id = models.URLField()

    class Meta:
        db_table = "mc_modpack"
