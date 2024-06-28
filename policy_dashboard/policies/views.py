#policies/views.py
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Policy
from .forms import PolicyForm
from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.core.mail import send_mail
from .models import Policy
from .forms import PolicyForm


import logging
logger = logging.getLogger(__name__)

def policy_list(request):
    """
    Display a list of all policies.

    Fetches all Policy objects from the database and renders them in the 'policy_list.html' template.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered 'policy_list.html' template with the list of policies.
    """
    policies = Policy.objects.all()
    return render(request, 'policies/policy_list.html', {'policies': policies})

def policy_create(request):
    """
    Handle creation of a new policy.

    If the request method is POST, it processes the form data and saves a new Policy object.
    If the request method is GET, it displays an empty form for creating a policy.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Redirects to 'policy_list' on successful creation, otherwise renders 'policy_form.html'.
    """
    if request.method == 'POST':
        form = PolicyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('policy_list')
    else:
        form = PolicyForm()
    return render(request, 'policies/policy_form.html', {'form': form})

def send_policy_issued_email(policy):
    """
    Send an email notification when a policy is issued.

    Constructs and sends an email to notify the customer that their policy has been issued.

    Args:
        policy (Policy): The Policy instance for which the email is being sent.

    Returns:
        None

    Logs:
        Logs an error message if the email fails to send.
    """
    subject = 'Your Policy Has Been Issued'
    message = f'Dear {policy.customer_name},\n\nYour policy has been issued.\n\nPolicy Number: {policy.policy_number}\n\nThank you for choosing our service.'
    email_from = settings.EMAIL_HOST_USER  # Sender's email address
    recipient_list = [settings.EMAIL_HOST_USER]  # For testing, sending to the same address
    try:
        send_mail(subject, message, email_from, recipient_list)
    except Exception as e:
        logger.error(f'Failed to send email to {policy.email}: {e}')

def policy_update(request, pk):
    """
    Handle updating an existing policy.

    If the request method is POST, it processes the form data and updates the Policy object.
    If the policy status is 'Policy Issued', it sends an email notification.
    If the request method is GET, it displays a form pre-filled with the policy data.

    Args:
        request (HttpRequest): The HTTP request object.
        pk (int): Primary key of the Policy to be updated.

    Returns:
        HttpResponse: Redirects to 'policy_list' on successful update, otherwise renders 'policy_form.html'.
    """
    policy = get_object_or_404(Policy, pk=pk)
    if request.method == 'POST':
        form = PolicyForm(request.POST, instance=policy)
        if form.is_valid():
            updated_policy = form.save()
            if updated_policy.policy_status == 'Policy Issued':
                send_policy_issued_email(updated_policy)
            return redirect('policy_list')
    else:
        form = PolicyForm(instance=policy)
    return render(request, 'policies/policy_form.html', {'form': form})

def policy_delete(request, pk):
    """
    Handle deletion of a policy.

    If the request method is POST, it deletes the Policy object and redirects to the policy list.
    If the request method is GET, it displays a confirmation page.

    Args:
        request (HttpRequest): The HTTP request object.
        pk (int): Primary key of the Policy to be deleted.

    Returns:
        HttpResponse: Redirects to 'policy_list' on successful deletion, otherwise renders 'policy_confirm_delete.html'.
    """
    policy = get_object_or_404(Policy, pk=pk)
    if request.method == 'POST':
        policy.delete()
        return redirect('policy_list')
    return render(request, 'policies/policy_confirm_delete.html', {'policy': policy})

def get_policy_fields(request):
    """
    Determine the visibility of certain fields based on policy type.

    Receives the policy type as a GET parameter and determines which fields should be visible.
    Returns the visibility status as a JSON response.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response containing visibility status of fields.
    """
    policy_type = request.GET.get('policy_type')

    # Determine which fields should be visible based on policy_type
    medical_type_visible = policy_type != 'ICICI'
    remarks_visible = policy_type == 'MAX'

    # Prepare JSON response
    response_data = {
        'medical_type_visible': medical_type_visible,
        'remarks_visible': remarks_visible,
    }

    return JsonResponse(response_data)
