# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class MergeCourse(models.Model):
    id= models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    instructor = models.CharField(max_length=80)
    learning_obj = models.CharField(max_length=40)
    course_contents = models.CharField(max_length=1000)
    teaching_methods = models.CharField(max_length=40)
    prerequisites = models.CharField(max_length=40)
    readings = models.CharField(max_length=40)
    applicability = models.CharField(max_length=80)
    workload = models.CharField(max_length=40)
    credits = models.CharField(max_length=40)
    time = models.CharField(max_length=40)
    evaluation = models.CharField(max_length=40)
    term = models.CharField(max_length=40)
    duration = models.CharField(max_length=40)
    course_type = models.CharField(max_length=400)
    medium_of_instruction = models.CharField(max_length=40)
    embedding=models.BinaryField(null=True)
    pass

    class Meta:
        db_table = 'merged_courses'  # This links to your existing table
        managed = False


# # Create your models here.
class CourseEra2(models.Model):
    id= models.IntegerField(primary_key=True)
    Course_name = models.CharField(max_length=255)
    University = models.CharField(max_length=255)
    Difficulty_Level = models.CharField(max_length=50)
    Course_Rating  = models.DecimalField(max_digits=4, decimal_places=1)
    Course_URL= models.URLField()
    Course_Description = models.TextField()
    Skills = models.TextField()
    embedding = models.BinaryField(null=True)

    class Meta:
        db_table ='coursera_2__2_'
        managed =False


class CourseCatalog(models.Model):
    id= models.IntegerField(primary_key=True)
    Year=models.IntegerField()
    Term=models.CharField(max_length=255)
    YearTerm=models.CharField(max_length=255)
    Subject=models.CharField(max_length=255)
    Number=models.IntegerField()
    Name=models.CharField(max_length=255)
    Description=models.TextField()
    Credit_Hours=models.CharField(max_length=255)
    Section_Info=models.CharField(max_length=255)
    Degree_Attributes=models.CharField(max_length=255)
    Schedule_Information=models.CharField(max_length=255)
    CRN=models.IntegerField()
    Section=models.CharField(max_length=255)
    Status_Code=models.CharField(max_length=255)
    Part_Of_Term=models.IntegerField()
    Section_Title=models.CharField(max_length=255)
    Section_Credit_Hours=models.CharField(max_length=255)
    Section_Status=models.CharField(max_length=255)
    Enrollment_Status=models.CharField(max_length=255)
    Type=models.CharField(max_length=255)
    Type_Code=models.CharField(max_length=255)
    Start_time = models.DateTimeField()
    End_Time = models.DateTimeField()
    Days_of_Week=models.CharField(max_length=255)
    Room=models.CharField(max_length=255)
    Building=models.CharField(max_length=255)
    instructor=models.CharField(max_length=255)
    embedding = models.BinaryField(null=True)

    class Meta:
        db_table = 'course_catalog__2_'
        managed = False

class Coursera(models.Model):
     id= models.IntegerField(primary_key=True)
     url=models.URLField()
     price=models.CharField(max_length=255)
     course_by=models.CharField(max_length=255)
     title=models.CharField(max_length=255)
     skills=models.CharField(max_length=255)
     ratings=models.DecimalField(max_digits=4, decimal_places=1)
     reviews=models.CharField(max_length=255)
     level_type_duration=models.CharField(max_length=255)
     embedding = models.BinaryField(null=True)


     class Meta:
         db_table = 'maincourse__2_'
         managed = False
#
# class CoursesData(models.Model):
#     id= models.IntegerField(primary_key=True)
#     CourseTitle=models.CharField(max_length=255)
#     Description=models.TextField()
#     Availability=models.CharField(max_length=255)
#     Cost=models.CharField(max_length=255)
#     embedding = models.BinaryField(null=True)
#
#     class Meta:
#         db_table = 'coursesdata__1_'
#         managed = False
#
#
# class EdX(models.Model):
#     id= models.IntegerField(primary_key=True)
#     Name=models.CharField(max_length=255)
#     University=models.CharField(max_length=255)
#     Difficulty_Level=models.CharField(max_length=255)
#     Link=models.URLField()
#     About=models.TextField()
#     Course_Description=models.TextField()
#     embedding = models.BinaryField(null=True)
#
#     class Meta:
#         db_table = 'edx__1_'
#         managed=False
#
# class Udemy_Courses(models.Model):
#     id= models.IntegerField(primary_key=True)
#     course_title=models.CharField(max_length=255)
#     url=models.URLField()
#     is_paid=models.BooleanField(default=True)
#     price=models.IntegerField()
#     num_subscribers=models.IntegerField()
#     level=models.CharField(max_length=255)
#     content_duration = models.DecimalField(max_digits=4, decimal_places=1)
#     published_timestamp=models.DateTimeField()
#     subject=models.CharField(max_length=255)
#     embedding = models.BinaryField(null=True)
#
#     class Meta:
#         db_table = 'udemy_courses_'
#         managed=False
#
#
#
#
















