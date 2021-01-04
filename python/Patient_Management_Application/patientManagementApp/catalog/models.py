from django.db import models

# Create your models here.
class Patient(models.Model): 
    unique_ID = models.CharField(max_length=20, unique=True, primary_key = True, help_text="Enter the patient's unique ID: ")
    first_Name = models.CharField(max_length=20, help_text="Enter the patient's first name: ")
    last_Name = models.CharField(max_length=20, help_text="Enter the patient's last name: ")
    date_of_birth = models.DateField(help_text="Enter the patient's date of birth: ")

    class Meta: 
        ordering = ['unique_ID', 'first_Name', 'last_Name', 'date_of_birth']

    def get_absolute_url(self): 
        """Returns the url to access a particular instance of Patient"""
        return reverse('patient-detail', args=[str(self.primary_key)])

    def __str__(self): 
        return f'{self.uniqueID}, {self.firstName}, {self.lastName}, {self.date_of_birth}'