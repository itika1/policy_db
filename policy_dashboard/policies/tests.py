from django.test import TestCase
from django.urls import reverse
from django.core import mail
from .models import Policy

class PolicyModelTest(TestCase):

    def setUp(self):
        self.policy = Policy.objects.create(
            policy_type='ICICI',
            application_number='APP001',
            customer_name='John Doe',
            email='john@example.com',
            phone_number='1234567890',
            date_of_birth='1990-01-01',
            policy_cover=100000.00,
            policy_status='Requirements Awaited',
        )

    def test_policy_creation(self):
        self.assertEqual(self.policy.customer_name, 'John Doe')
        self.assertEqual(self.policy.policy_type, 'ICICI')
        self.assertEqual(self.policy.medical_type, None)
        self.assertEqual(self.policy.medicals_status, None)

    def test_policy_str(self):
        self.assertEqual(str(self.policy), 'ICICI - APP001')

    def test_policy_clean(self):
        self.policy.policy_type = 'MAX'
        self.policy.remarks = 'This is a test remark'
        self.policy.save()
        self.assertEqual(self.policy.remarks, None)


class PolicyAdminTest(TestCase):

    def setUp(self):
        self.policy = Policy.objects.create(
            policy_type='ICICI',
            application_number='APP002',
            customer_name='Jane Doe',
            email='jane@example.com',
            phone_number='0987654321',
            date_of_birth='1985-01-01',
            policy_cover=200000.00,
            policy_status='Policy Issued',
            policy_number='POL123',
        )

    def test_policy_issued_email_sent(self):
        self.assertEqual(len(mail.outbox), 1)
        email = mail.outbox[0]
        self.assertEqual(email.subject, 'Your Policy Has Been Issued')
        self.assertIn('Dear Jane Doe', email.body)
        self.assertIn('POL123', email.body)

class PolicyViewsTest(TestCase):

    def setUp(self):
        self.policy = Policy.objects.create(
            policy_type='HDFC',
            application_number='APP003',
            customer_name='Alice',
            email='alice@example.com',
            phone_number='1122334455',
            date_of_birth='1970-01-01',
            policy_cover=300000.00,
            policy_status='Requirements Closed',
        )

    def test_policy_list_view(self):
        response = self.client.get(reverse('policy_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Alice')
        self.assertTemplateUsed(response, 'policies/policy_list.html')

    def test_policy_create_view(self):
        response = self.client.post(reverse('policy_create'), {
            'policy_type': 'HDFC',
            'application_number': 'APP004',
            'customer_name': 'Bob',
            'email': 'bob@example.com',
            'phone_number': '5566778899',
            'date_of_birth': '1980-01-01',
            'policy_cover': 400000.00,
            'policy_status': 'Underwriting',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Policy.objects.count(), 2)

    def test_policy_update_view(self):
        response = self.client.post(reverse('policy_update', args=[self.policy.id]), {
            'policy_type': 'HDFC',
            'application_number': 'APP003',
            'customer_name': 'Alice Updated',
            'email': 'alice_updated@example.com',
            'phone_number': '1122334455',
            'date_of_birth': '1970-01-01',
            'policy_cover': 300000.00,
            'policy_status': 'Policy Issued',
        })
        self.assertEqual(response.status_code, 302)
        self.policy.refresh_from_db()
        self.assertEqual(self.policy.customer_name, 'Alice Updated')
        self.assertEqual(self.policy.policy_status, 'Policy Issued')
        self.assertEqual(len(mail.outbox), 1)

    def test_policy_delete_view(self):
        response = self.client.post(reverse('policy_delete', args=[self.policy.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Policy.objects.count(), 0)
