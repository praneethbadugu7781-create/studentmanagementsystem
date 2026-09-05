import re
from django import forms
from .models import Student

DEGREE_CHOICES = [
    ('', '-- Select Degree Course --'),
    ('B.Sc (Computer Science)', 'B.Sc (Computer Science)'),
    ('B.Sc (Data Science)', 'B.Sc (Data Science)'),
    ('B.Sc (Mathematics, Statistics, Computers)', 'B.Sc (Mathematics, Statistics, Computers)'),
    ('B.Sc (Physics, Chemistry, Mathematics)', 'B.Sc (Physics, Chemistry, Mathematics)'),
    ('B.Sc (Electronics)', 'B.Sc (Electronics)'),
    ('B.Sc (Biotechnology)', 'B.Sc (Biotechnology)'),
    ('B.Com (Computer Applications)', 'B.Com (Computer Applications)'),
    ('B.Com (General)', 'B.Com (General)'),
    ('B.Com (Finance & Taxation)', 'B.Com (Finance & Taxation)'),
    ('BCA (Bachelor of Computer Applications)', 'BCA (Bachelor of Computer Applications)'),
    ('BBA (Bachelor of Business Administration)', 'BBA (Bachelor of Business Administration)'),
    ('B.A (Economics, History, Politics)', 'B.A (Economics, History, Politics)'),
    ('B.A (English Literature)', 'B.A (English Literature)'),
]


class StudentForm(forms.ModelForm):
    """
    Form for adding and editing Student records with Bootstrap styling and custom validation.
    Strictly Degree courses (B.Sc, B.Com, BCA, BBA, B.A).
    """
    course = forms.ChoiceField(
        choices=DEGREE_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-select',
        }),
        label='Degree Course'
    )

    class Meta:
        model = Student
        fields = ['name', 'roll_number', 'email', 'course', 'phone']
        labels = {
            'name': 'Full Name',
            'roll_number': 'Roll Number',
            'email': 'Email Address',
            'course': 'Degree Course',
            'phone': 'Phone Number',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter student's full name",
                'autocomplete': 'off',
            }),
            'roll_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter roll number (e.g. 21DEG001)',
                'autocomplete': 'off',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'student@example.com',
                'autocomplete': 'off',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter phone number (e.g. 9876543210)',
                'autocomplete': 'off',
            }),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone', '').strip()
        digits_only = re.sub(r'\D', '', phone)
        if not digits_only or len(digits_only) < 7 or len(digits_only) > 15:
            raise forms.ValidationError("Please enter a valid phone number (7 to 15 digits).")
        return phone

    def clean_roll_number(self):
        roll_number = self.cleaned_data.get('roll_number', '').strip().upper()
        if not roll_number:
            raise forms.ValidationError("Roll number is required.")
        
        # Check uniqueness on create or when changed on update
        instance_pk = self.instance.pk if self.instance else None
        qs = Student.objects.filter(roll_number__iexact=roll_number)
        if instance_pk:
            qs = qs.exclude(pk=instance_pk)
        if qs.exists():
            raise forms.ValidationError(f"A student with roll number '{roll_number}' already exists.")
        
        return roll_number
