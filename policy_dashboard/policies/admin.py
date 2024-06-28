from django.contrib import admin
from .models import Policy



@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    """
    Custom admin interface for the Policy model.

    Attributes:
        list_display (list): Fields to display in the admin list view.
        search_fields (tuple): Fields that can be searched in the admin list view.
        list_filter (list): Fields that can be filtered in the admin list view.
        list_per_page (int): Number of items to display per page in the admin list view.
    """
    list_display = ['policy_type', 'customer_name', 'policy_status']
    search_fields = ('customer_name', 'application_number')
    list_filter = ['policy_status', 'customer_name', 'created_at']
    list_per_page = 3 

    def get_form(self, request, obj=None, **kwargs):
        """
        Customizes the form used in the admin interface for adding/editing policies.

        Args:
            request (HttpRequest): The current request object.
            obj (Policy): The instance of the Policy model being edited, or None if adding a new instance.

        Returns:
            forms.ModelForm: The form instance with customized widget attributes.
        """
        form = super().get_form(request, obj, **kwargs)
        if obj:  # Editing an existing policy
            initial_policy_type = obj.policy_type
        else:  # Adding a new policy
            initial_policy_type = None

        # Set initial visibility based on policy_type
        form.base_fields['medical_type'].widget.attrs['class'] = 'hidden' if initial_policy_type == 'ICICI' else ''
        form.base_fields['medicals_status'].widget.attrs['class'] = 'hidden' if initial_policy_type == 'ICICI' else ''
        form.base_fields['remarks'].widget.attrs['class'] = 'hidden' if initial_policy_type == 'MAX' else ''

        # Add JavaScript to handle onchange event of policy_type
        form.base_fields['policy_type'].widget.attrs['onchange'] = 'showHideFields();'
        return form

    class Media:
        # Include custom JavaScript file
        js = ('js/policy_admin.js',)

