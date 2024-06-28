# policies/models.py

from django.db import models


class Policy(models.Model):
    """
    A model representing a life insurance policy.

    Attributes:
        POLICY_TYPE_CHOICES (list): Choices for the type of policy.
        APPLICATION_STATUS_CHOICES (list): Choices for the status of the application.
        MEDICAL_TYPE_CHOICES (list): Choices for the type of medical examination.
        MEDICAL_STATUS_CHOICES (list): Choices for the status of the medical examination.
        policy_type (CharField): The type of the policy.
        application_number (CharField): The application number of the policy.
        customer_name (CharField): The name of the customer.
        email (EmailField): The email address of the customer.
        phone_number (CharField): The phone number of the customer.
        date_of_birth (DateField): The date of birth of the customer.
        policy_cover (DecimalField): The coverage amount of the policy.
        policy_status (CharField): The status of the policy application.
        policy_number (CharField): The policy number (optional).
        medical_type (CharField): The type of medical examination (optional).
        medicals_status (CharField): The status of the medical examination (optional).
        remarks (TextField): Any additional remarks (optional).
        created_at (DateTimeField): The date and time when the policy was created.
    """
    POLICY_TYPE_CHOICES = [
        ('ICICI', 'ICICI Life'),
        ('MAX', 'Max Life'),
        ('HDFC', 'HDFC Life'),
    ]

    APPLICATION_STATUS_CHOICES = [
        ('Requirements Awaited', 'Requirements Awaited'),
        ('Requirements Closed', 'Requirements Closed'),
        ('Underwriting', 'Underwriting'),
        ('Policy Issued', 'Policy Issued'),
        ('Policy Rejected', 'Policy Rejected'),
    ]
    
    MEDICAL_TYPE_CHOICES = [
        ('Tele Medicals', 'Tele Medicals'),
        ('Physical Medicals', 'Physical Medicals'),
    ]
    
    MEDICAL_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Scheduled', 'Scheduled'),
        ('Waiting for Report', 'Waiting for Report'),
        ('Done', 'Done'),
    ]

    policy_type = models.CharField(max_length=50, choices=POLICY_TYPE_CHOICES)
    application_number = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    policy_cover = models.DecimalField(max_digits=10, decimal_places=2)
    policy_status = models.CharField(max_length=50, choices=APPLICATION_STATUS_CHOICES)
    policy_number = models.CharField(max_length=100, blank=True, null=True)
    medical_type = models.CharField(max_length=50, choices=MEDICAL_TYPE_CHOICES, blank=True, null=True)
    medicals_status = models.CharField(max_length=50, choices=MEDICAL_STATUS_CHOICES, blank=True, null=True)
    remarks = models.TextField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Add this line

    def clean(self):
        """
        Custom validation to clear fields based on the policy type.
        If the policy type is 'ICICI', it clears the medical_type and medicals_status fields.
        If the policy type is 'MAX', it clears the remarks field.
        """
        if self.policy_type == 'ICICI':
            self.medical_type = None
            self.medical_status = None
        if self.policy_type == 'MAX':
            self.remarks = None

        super().clean()

    def save(self, *args, **kwargs):
        """
        Overrides the save method to include custom validation before saving.
        """
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of the Policy instance.
        """
        return f'{self.policy_type} - {self.application_number}'