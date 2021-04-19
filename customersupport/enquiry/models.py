from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Enquiry(models.Model):
    mobile_regex = RegexValidator(r'^[789]\d{9}$', 'Invalid contact number.')
    email_regex = RegexValidator(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)','Enter a valid email address.')

    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=255,null=False, blank=False,validators=[email_regex])
    mobile = models.CharField(null=False,blank=False,validators=[mobile_regex], max_length=15,verbose_name="Mobile No.")
    query = models.TextField(null=False,blank=False)

    class Meta:
        db_table = "enquiry"
