from datetime import timezone
from django.db import models

# from account.models import User
from course.models import Course

# Create your models here.


class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')
    title = models.CharField(max_length=255)
    order = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)




    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Module'
        verbose_name_plural = 'Modules'


       

    def __str__(self):
        return self.title

