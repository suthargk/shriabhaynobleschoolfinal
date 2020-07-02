from django.db import models
from django.contrib.auth.models import User
#from Nobles.models import Homework
# Create your models here.


class Classroom(models.Model):
    classroom = models.CharField(max_length=100)
    cid = models.IntegerField(null=True)
    
    def __str__(self):
        return self.classroom
    class Meta:
        ordering = ['cid']
        verbose_name_plural = "Classroom"

class Subjects(models.Model):
    subject_name = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.subject_name
    


class Lectures(models.Model):
    topic = models.CharField(max_length = 100)
    video_detail = models.TextField(blank=True, null=True)
    video = models.FileField(upload_to = 'files/')
    classroom = models.ForeignKey('Elearning.Classroom', on_delete=models.CASCADE)
    subject = models.ForeignKey('Elearning.Subjects', on_delete=models.CASCADE)
    homework = models.ManyToManyField('Nobles.Homeworks')

    def __str__(self):
        return self.topic
