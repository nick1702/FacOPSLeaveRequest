from django.db import models
from django.urls import reverse
# Create your models here.


class SubmissionObject(models.Model):
    """Abstract Submission Object storing individual submission data"""

    status = models.CharField(max_length=200)

    userName = models.CharField(max_length=200)

    lastModified = models.DateTimeField(auto_now=True)



    #Methods
    def get_absolute_url(self):
        """Returns the URL to access particular instance of a submission"""
        return reverse('model-detail-view', args=[str(self.id)])

class Reason(models.Model):
    """Reason for leave request"""

    #Fields
    reason = models.CharField(max_length=200, help_text='Enter a reason for this leave request')

    def __str__(self):
        """String for representing submission object"""
        return self.reason