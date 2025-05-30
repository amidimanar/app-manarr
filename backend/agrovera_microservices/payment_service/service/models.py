from django.db import models

class MemberPayment(models.Model):
    name = models.CharField(max_length=100, default="Unknown")
    phone = models.CharField(max_length=25, default='0000000000')
    payment_status = models.CharField(
        max_length=10,
        choices=[
            ('paid', 'A payé'),
            ('not_paid', "N'a pas payé")  # ✅ fixed: double quotes around French text
        ],
        default='not_paid'
    )
    payment_date = models.DateField(null=True, blank=True)

