from django import forms
from .models import Policy

class PolicyForm(forms.ModelForm):
    """
    Form for the Policy model.

    This form is used to create and update Policy instances. It includes the fields
    'policy_type', 'medical_type', 'medicals_status', and 'remarks'.

    Attributes:
        model (Model): The model that this form is for.
        fields (tuple): The fields to include in the form.
    """
    class Meta:
        """
        Meta options for the PolicyForm.

        Attributes:
            model (Model): The model that this form is for.
            fields (tuple): The fields to include in the form.
        """
        model = Policy
        fields = ('policy_type', 'medical_type', 'medicals_status', 'remarks')