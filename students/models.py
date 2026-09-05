from django.db import models


class Student(models.Model):
    """
    Student model representing individual student records in the system.
    Core fields: Name, Roll Number, Email, Course, Phone.
    """
    name = models.CharField(max_length=100, verbose_name="Full Name")
    roll_number = models.CharField(max_length=20, unique=True, verbose_name="Roll Number")
    email = models.EmailField(verbose_name="Email Address")
    course = models.CharField(max_length=100, verbose_name="Course")
    phone = models.CharField(max_length=15, verbose_name="Phone Number")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.roll_number})"

    @property
    def initial(self):
        """Returns the first uppercase letter of the student's name for avatar rendering."""
        if self.name and len(self.name.strip()) > 0:
            return self.name.strip()[0].upper()
        return "S"

