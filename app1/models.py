from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255)
    roll_no = models.IntegerField()
    

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name=models.CharField(max_length=100)
    teacher_id=models.IntegerField()

    def __str__(self):
        return str(self.teacher_id)
   