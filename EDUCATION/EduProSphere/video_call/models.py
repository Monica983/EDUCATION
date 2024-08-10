from datetime import timezone
from django.db import models

from EduProSphere.account.models import User

# Create your models here.


class Lesson(models.Model):
    id = models.AutoField(primary_key=True)
    module = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=255)
    video_url = models.URLField()
    content = models.TextField(blank=True, null=True)
    order = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'

    def __str__(self):
        return self.title
