# Policy Dashboard

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Supported Policies](#supported-policies)
- [Technologies Used](#technologies-used)
- [Level Accomplished](#level-accomplished)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Admin Customization](#admin-customization)
- [Form Customization](#form-customization)
- [Signals](#signals)
- [Database](#database)
- [Views](#views)
- [License](#license)

## Description
This is a Django-based application for managing insurance policies. The application allows the admin to create, edit, delete, and list policies with pagination. The system also sends an automated email when a policy is issued.

## Features
- CRUD operations on policies
- Pagination on policy list view
- Conditional form fields based on policy type
- Automated email notification on policy issuance

## Supported Policies
1. ICICI Life
2. Max Life
3. HDFC Life


## Technologies Used
- Django
- SQLite
- Django Rest Framework (for API endpoints)
- Python SMTP (for sending emails)

## Level Accomplished

2/3 levels are accomplished.
### Level 1
Admin Views (or) Only APIs to perform the following actions.

● Allow admin to create, edit & delete the policy.

● List out all the policies (with pagination).

● Filter policies using the following things

○ Policy Status

○ Customer Name

○ Created date

### Level 2

● When a policy is issued send an automated email to the customer email.

## Setup Instructions

### Prerequisites
- Python 3.x
- Django 3.x or later
- Virtualenv (optional but recommended)

### Installation

1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd policy_dashboard
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```sh
    python manage.py migrate
    ```

5. Create a superuser for accessing the admin interface:
    ```sh
    python manage.py createsuperuser
    ```
    The used:
    1) username: itika, 
    2) password: adminDitto

6. Collect static files:
    ```sh
    python manage.py collectstatic
    ```

7. Run the development server:
    ```sh
    python manage.py runserver
    ```

## Usage

- Access the admin interface at `http://127.0.0.1:8000/admin/`.
- Use the superuser credentials to log in.
- Add, edit, delete, and list policies as needed.

## Email Notifications

When a policy is issued, an automated email is sent to the customer's email address. Ensure you have configured your email settings in `settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_app_specific_password'
```
Google may block sign-ins from some apps or devices that do not use modern security standards. To allow your Django app to send emails through your Gmail account, you might need to allow less secure apps:

Go to your Google Account settings.
Navigate to the Security section.
Under "Less secure app access," turn on "Allow less secure apps."
Alternatively, you can set up an App Password for added security:

Go to your Google Account settings.
Navigate to the Security section.
Under "Signing in to Google," enable 2-Step Verification.
After enabling 2-Step Verification, create an App Password specifically for your Django application.

## Admin Customization

The `PolicyAdmin` class in `policies/admin.py` customizes the Django admin interface for the `Policy` model:

- `list_display`: Specifies the fields to be displayed in the list view.
- `search_fields`: Fields that can be searched.
- `list_filter`: Filters available in the sidebar.
- `list_per_page`: Pagination setting for the admin list view.
- `get_form`: Customizes the form based on the policy type.

## Form Customization

The `PolicyForm` class in `policies/forms.py` is a `ModelForm` for the `Policy` model:

- Customizes which fields are displayed in the form.


## Signals

The `send_policy_issued_email` function in `policies/signals.py` sends an email notification when a policy is issued:

- Uses Django's `post_save` signal to trigger the email when the policy status is 'Policy Issued'.

## Database

This project uses SQLite as the database, configured through Django's ORM. The SQLite database file (`db.sqlite3`) will be created automatically when migrations are applied.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.