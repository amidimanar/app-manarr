from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from service.models import Member

class MemberAPITest(APITestCase):

    def setUp(self):
        self.member = Member.objects.create(
            name="Rayen Test",
            telephone="123456789",
            email="rayen@example.com",
            activity_type="culture"
        )
        self.url_list = reverse('member-list')  # /member/
        self.url_detail = reverse('member-detail', args=[self.member.id])  # /member/<id>/

    def test_create_member(self):
        data = {
            "name": "New Member",
            "telephone": "987654321",
            "email": "new@example.com",
            "activity_type": "elevage"
        }
        response = self.client.post(self.url_list, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Member.objects.count(), 2)
        self.assertEqual(Member.objects.latest('id').name, "New Member")

    def test_get_all_members(self):
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    def test_get_single_member(self):
        response = self.client.get(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.member.name)

    def test_update_member(self):
        response = self.client.patch(self.url_detail, {"name": "Updated"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.member.refresh_from_db()
        self.assertEqual(self.member.name, "Updated")

    def test_delete_member(self):
        response = self.client.delete(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Member.objects.filter(id=self.member.id).exists())
