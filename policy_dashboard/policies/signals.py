# policies/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Policy

@receiver(post_save, sender=Policy)
def send_policy_issued_email(sender, instance, **kwargs):
    """
    Signal handler to send an email notification when a policy is issued.

    This function is called whenever a Policy instance is saved. If the policy status is 'Policy Issued',
    it sends an email to the customer notifying them that their policy has been issued and includes the policy number.

    Args:
        sender (Model): The model class that sent the signal.
        instance (Policy): The actual instance being saved.
        **kwargs: Additional keyword arguments.

    Returns:
        None
    """
    if instance.policy_status == 'Policy Issued':
        subject = 'Your Policy Has Been Issued'
        message = f'Hello {instance.customer_name},\n\nYour policy with the application number {instance.application_number} has been issued. Your policy number is {instance.policy_number}.\n\nThank you for choosing our service.\n\nBest regards,\nYour Insurance Company'
        recipient_list = [instance.email]
        
        send_mail(subject, message, 'no-reply@insurancecompany.com', recipient_list)
