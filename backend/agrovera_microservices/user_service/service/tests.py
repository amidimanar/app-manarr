# service/tests.py

from django.test import TestCase
from service.models import Member

class MemberModelTest(TestCase):
    def setUp(self):
        self.member = Member.objects.create(
            name="Test User",
            telephone="1234567890",
            email="test@example.com",
            activity_type="culture"
        )

    def test_member_creation(self):
        self.assertEqual(self.member.name, "Test User")
        self.assertEqual(self.member.telephone, "1234567890")
        self.assertEqual(self.member.email, "test@example.com")
        self.assertEqual(self.member.activity_type, "culture")
