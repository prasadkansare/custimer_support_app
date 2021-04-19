from django.db import models
from enquiry.models import Enquiry
from django.contrib.humanize.templatetags.humanize import naturalday
from django.utils import timezone

# Create your models here.

class Feedback(models.Model):
    enquiry = models.ForeignKey(Enquiry,null=True, blank=True,on_delete=models.CASCADE)
    feedback = models.TextField(null=False,blank=False)
    created_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(default=naturalday(timezone.now))
    updated_by = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True,null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = "feedback"

    def delete(self):  
        self.deleted_at=timezone.now()
        self.save()


class Review(models.Model):
    TYPE_CHOICES_STATUS = (
        ('SATISFIED','Satisfied'),
        ('UNSATISFIED','Unsatisfied'),
    )
    feedback = models.ForeignKey(Feedback,null=True, blank=True,on_delete=models.CASCADE)
    review = models.CharField(max_length=100,null=False,blank=False, choices=TYPE_CHOICES_STATUS)
    link = models.CharField(max_length=100,blank=True,null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(default=naturalday(timezone.now))
    updated_by = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True,null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = "review"

    def delete(self):  
        self.deleted_at=timezone.now()
        self.save()
