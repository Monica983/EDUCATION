from datetime import timezone
from django.db import models
from account.models import Course, Lesson, Module, User


# Create your models here.



class UserProgress(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='progress')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='user_progress')
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='user_progress', null=True, blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='user_progress', null=True, blank=True)
    progress_percentage = models.IntegerField()
    quiz_score = models.IntegerField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)



    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'userprogress'
        verbose_name_plural = 'userprogresses'

    def __str__(self) -> str:
        return self.user.firstname