from django.db import models

# Create your models here.
class Patient(models.Model): 
    uniqueID = models.CharField(max_length=20, help_text="Enter the patient's unique ID: ")
    firstName = models.CharField(max_length=20, help_text="Enter the patient's unique ID: ")
    lastName = models.CharField(max_length=20, help_text="Enter the patient's unique ID: ")
    dob = models.CharField(max_length=20, help_text="Enter the patient's unique ID: ")

    class Meta: 
        ordering = ['-uniqueID', '-firstName', '-lastName', '-dob']

    def get_absolute_url(self): 
        """Returns the url to access a particular instance of Patient"""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self): 
        return (self.uniqueID, self.firstName, self.lastName, self.dob)