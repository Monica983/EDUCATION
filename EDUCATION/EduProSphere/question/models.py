from datetime import timezone
from django.db import models

from EduProSphere.account.models import Quiz

# Create your models here.


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()
    correct_answer = models.CharField(max_length=1000)
    marks = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question_text
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'


