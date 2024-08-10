from datetime import timezone
from django.db import models
from account.models import Course, User

# Create your models here.




class Discussion(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='discussions')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='discussions')
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Discussion'
        verbose_name_plural = 'Discussions'