from datetime import timezone
from django.db import models

from EduProSphere.account.models import Course

# Create your models here.



class Quiz(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='quizzes')
    title = models.CharField(max_length=255)
    total_marks = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Quize'
        verbose_name_plural = 'Quizes'
