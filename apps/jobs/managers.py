from django.db import models


class ActiveJobManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=self.model.JobStatus.ACTIVE)
