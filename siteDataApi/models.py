from django.db import models
from django.contrib import admin

class Service(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField(max_length = 1000)

    def __str__(self) -> str:
        return f"{self.name}"


class TeamMember(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    birthday = models.DateField()
    service_area = models.ForeignKey(Service, 
        on_delete = models.SET_NULL , null = True, blank = True)
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @property
    @admin.display(
        ordering='last_name',
        description='Full name of the person',
    )
    def full_name(self):
        return self.first_name + ' ' + self.last_name

class BlogPost(models.Model):
    headline = models.CharField(max_length = 100)
    content = models.TextField(max_length = 1000)
    pub_date = models.DateField(auto_created=True)
    last_modified = models.DateField(auto_now=True)
    author = models.ForeignKey(TeamMember, 
        on_delete = models.SET_NULL , null = True, blank = True)

    def __str__(self) -> str:
        return f"{self.headline}"
