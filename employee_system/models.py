import datetime
from django.db import models
from django.core.validators import RegexValidator, FileExtensionValidator
from django.core.exceptions import ValidationError
from django.conf import settings
from django.urls import reverse


def account_file_size(uploaded_file):
    max_size_in_mb = int(settings.ACCOUNT_MAX_FILE_SIZE_UPLOAD / (1024 * 1024))
    if uploaded_file.size > settings.ACCOUNT_MAX_FILE_SIZE_UPLOAD:
        raise ValidationError(_("File too large. Size should not exceed {} MiB.".format(str(max_size_in_mb))))


class Employee(models.Model):
    mobile_validator = RegexValidator(regex=r'^\d{6,20}$',
                                      message="Mobile Number length must be between 6 and 20 numbers")
    extension_error_message = "Allowed file types: pdf, jpg, jpeg, png"
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    TYPE_CHOICES = (
        ('P', 'Permenant'),
        ('T', 'Temporary')
    )
    # you can make employee_code unique , but for testing import/export purposing may cause conflicts
    employee_code = models.CharField(max_length=60, blank=True)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birth_date = models.DateField(blank=False, null=False)
    # you can make email unique , but for testing import/export purposing may cause conflicts
    email = models.EmailField(blank=False, null=False)
    # you can make mobile unique , but for testing import/export purposing may cause conflicts
    mobile = models.CharField(max_length=50, blank=False, null=True, validators=[mobile_validator],
                              verbose_name='Mobile Number')
    hire_date = models.DateField(blank=False, null=False)
    employee_type = models.CharField(max_length=1, choices=TYPE_CHOICES, blank=False, null=False)
    photo = models.ImageField(blank=True, null=True, upload_to='employees_images', validators=[FileExtensionValidator(
        allowed_extensions=['pdf', 'jpg', 'jpeg', 'png'], message=extension_error_message), account_file_size])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def account_file_size(cls, uploaded_file):
        max_size_in_mb = int(settings.ACCOUNT_MAX_FILE_SIZE_UPLOAD / (1024 * 1024))
        if uploaded_file.size > settings.ACCOUNT_MAX_FILE_SIZE_UPLOAD:
            raise ValidationError("File too large. Size should not exceed {} MiB.".format(str(max_size_in_mb)))
    
    def get_absolute_url(self):
        return reverse('employees:show-employee', args=[self.id])

    # for auto generating unique employee_code
    def save(self, *args, **kwargs):
        if not self.employee_code:
            self.employee_code = self.first_name[:2] + self.mobile[5:] + self.email[:5] + datetime.now().time[8:]
        return super().save()

    class Meta:
        verbose_name = 'employee'
        verbose_name_plural = "employees"
        ordering = ("-created_at",)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)