# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Departments(models.Model):
    deptID = models.PositiveIntegerField(
        primary_key=True,
        null=False,
        editable=False
    )
    name = models.TextField(
        max_length=255
    )
    def __str__(self):
        return 'Dept ID:' + str(self.deptID)

class Interests(models.Model):

    interestID = models.PositiveIntegerField(
        primary_key=True,
        null=False,
        editable=False
    )
    name = models.TextField(
        max_length=255
    )
    def __str__(self):
        return 'Interest ID:' + str(self.interestID)

class Users(models.Model):
    ACTIVE = 1
    DEACTIVE = 2
    STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (DEACTIVE, 'Deactive')
    )

    STUDENT = 0
    TUTOR = 1
    OCCUPATION = (
        (STUDENT, 'Student'),
        (TUTOR, 'Tutor')
    )

    userID = models.PositiveIntegerField(
        primary_key=True,
        null=False,
        editable=False
    )
    email = models.EmailField(
        max_length=30,
        default=''
    )
    status = models.SmallIntegerField(
        choices=STATUS_CHOICES
    )
    password = models.TextField(
        max_length=255
    )
    isTutor = models.PositiveIntegerField(
        choices=OCCUPATION,
        default=''
    )
    isStudent = models.PositiveIntegerField(
        choices=OCCUPATION,
        default=''
    )
    deptID = models.ForeignKey(
        Departments,
        on_delete=models.CASCADE
    )
    def __str__(self):
        return 'refers to departments reference:' + self.Departments.deptID

class UserInterests(models.Model):
        userID = models.ForeignKey(
            'Users',
            on_delete=models.CASCADE
        )
        interestID = models.ForeignKey(
            'Interests',
            on_delete=models.CASCADE
        )
        def __str__(self):
            return 'refers to departments reference:' + self.Interests.interestID + self.Users.userID