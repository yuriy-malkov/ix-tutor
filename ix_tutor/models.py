# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.db import models

# Create your models here.

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

    userID = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
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
    isTutor = models.SmallIntegerField(
        choices=OCCUPATION,
        default=''
    )
    isStudent = models.SmallIntegerField(
        choices=OCCUPATION,
        default=''
    )
    deptID = models.ForeignKey(
        Departments
    )
    def __str__(self):
        return 'refers to departments reference:' + self.Departments.deptID

class Departments(models.Model):

    deptID = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.TextField(
        max_length=255
    )

    def __str__(self):
        return 'Dept ID:' + str(self.deptID)