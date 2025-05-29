from django.db import models

# Define a model to store booking information for the Paw Spa
class Booking(models.Model):

    # Choices for the available grooming services
    SERVICE_CHOICES = [
        ('Bath', 'Bath'),
        ('Haircut', 'Haircut'),
        ('Nail Trim', 'Nail Trim'),
        ('Full Grooming', 'Full Grooming'),
    ]

    # Choices for booking status
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('declined', 'Declined'),
    ]

    # Owner's contact information
    owner_name = models.CharField(max_length=100)  
    email = models.EmailField()                    
    phone_number = models.CharField(max_length=15)  

    # Pet's booking details
    pet_name = models.CharField(max_length=100)  
    pet_type = models.CharField(max_length=100)  
    service = models.CharField(
        max_length=100, choices=SERVICE_CHOICES)  
    date = models.DateField()                     

    # Booking status
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    # This function defines how each booking will be displayed as a string
    def __str__(self):
        return f"{self.owner_name} - {self.pet_type} - {self.service} ({self.status})" 


