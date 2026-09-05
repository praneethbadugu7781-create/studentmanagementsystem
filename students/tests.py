from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.admin.sites import site
from .models import Student
from .forms import StudentForm


class StudentModelTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            name="Rahul Verma",
            roll_number="21BSC501",
            email="rahul.verma@example.com",
            course="B.Sc (Computer Science)",
            phone="9876543210"
        )

    def test_student_str_representation(self):
        self.assertEqual(str(self.student), "Rahul Verma (21BSC501)")

    def test_student_initial_property(self):
        self.assertEqual(self.student.initial, "R")
        empty_name_student = Student(name="")
        self.assertEqual(empty_name_student.initial, "S")


class StudentFormTest(TestCase):
    def test_valid_student_form(self):
        data = {
            'name': 'Kavita Singh',
            'roll_number': '21BCA502',
            'email': 'kavita.singh@example.com',
            'course': 'BCA (Bachelor of Computer Applications)',
            'phone': '+91 9876543210'
        }
        form = StudentForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_email_form(self):
        data = {
            'name': 'Kavita Singh',
            'roll_number': '21BCA502',
            'email': 'not-an-email',
            'course': 'BCA (Bachelor of Computer Applications)',
            'phone': '9876543210'
        }
        form = StudentForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_invalid_phone_form(self):
        data = {
            'name': 'Kavita Singh',
            'roll_number': '21BCA502',
            'email': 'kavita@example.com',
            'course': 'BCA (Bachelor of Computer Applications)',
            'phone': '123'  # Too short
        }
        form = StudentForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('phone', form.errors)

    def test_duplicate_roll_number_validation(self):
        Student.objects.create(
            name="Existing Student",
            roll_number="21DUP001",
            email="existing@example.com",
            course="B.Sc (Computer Science)",
            phone="9876543210"
        )
        data = {
            'name': 'New Student',
            'roll_number': '21dup001',
            'email': 'new@example.com',
            'course': 'B.Com (General)',
            'phone': '9876543211'
        }
        form = StudentForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('roll_number', form.errors)


class StudentViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.student1 = Student.objects.create(
            name="Alice Wonder",
            roll_number="21BSC001",
            email="alice@example.com",
            course="B.Sc (Computer Science)",
            phone="9876543210"
        )
        self.student2 = Student.objects.create(
            name="Bob Builder",
            roll_number="21BCOM002",
            email="bob@example.com",
            course="B.Com (General)",
            phone="9123456780"
        )

    def test_dashboard_view(self):
        response = self.client.get(reverse('students:dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard.html')
        self.assertEqual(response.context['total_students'], 2)
        self.assertEqual(response.context['courses_count'], 2)
        self.assertEqual(response.context['records_count'], 2)
        self.assertContains(response, "Alice Wonder")
        self.assertContains(response, "Bob Builder")

    def test_student_list_view(self):
        response = self.client.get(reverse('students:student_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'students/student_list.html')
        self.assertEqual(len(response.context['students']), 2)

    def test_student_list_search(self):
        # Search by name
        response = self.client.get(reverse('students:student_list'), {'q': 'Alice'})
        self.assertEqual(len(response.context['students']), 1)
        self.assertEqual(response.context['students'][0].name, "Alice Wonder")

        # Search by roll number
        response = self.client.get(reverse('students:student_list'), {'q': '21BCOM002'})
        self.assertEqual(len(response.context['students']), 1)
        self.assertEqual(response.context['students'][0].name, "Bob Builder")

        # Search by course
        response = self.client.get(reverse('students:student_list'), {'q': 'B.Com'})
        self.assertEqual(len(response.context['students']), 1)

        # Search non-matching term
        response = self.client.get(reverse('students:student_list'), {'q': 'NonExistent'})
        self.assertEqual(len(response.context['students']), 0)
        self.assertContains(response, "No student records match")

    def test_student_detail_view(self):
        response = self.client.get(reverse('students:student_detail', kwargs={'pk': self.student1.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'students/student_detail.html')
        self.assertContains(response, "Alice Wonder")
        self.assertContains(response, "21BSC001")

    def test_student_detail_404(self):
        response = self.client.get(reverse('students:student_detail', kwargs={'pk': 99999}))
        self.assertEqual(response.status_code, 404)

    def test_student_create_view_get(self):
        response = self.client.get(reverse('students:student_add'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'students/student_form.html')

    def test_student_create_view_post_valid(self):
        data = {
            'name': 'Charlie Chaplin',
            'roll_number': '21BCA003',
            'email': 'charlie@example.com',
            'course': 'BCA (Bachelor of Computer Applications)',
            'phone': '9898989898'
        }
        response = self.client.post(reverse('students:student_add'), data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Student.objects.filter(roll_number='21BCA003').exists())
        self.assertContains(response, "added successfully")

    def test_student_update_view(self):
        data = {
            'name': 'Alice Wonder Updated',
            'roll_number': '21BSC001',
            'email': 'alice.updated@example.com',
            'course': 'B.Sc (Data Science)',
            'phone': '9876543210'
        }
        response = self.client.post(
            reverse('students:student_edit', kwargs={'pk': self.student1.pk}),
            data=data,
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.student1.refresh_from_db()
        self.assertEqual(self.student1.name, "Alice Wonder Updated")
        self.assertEqual(self.student1.course, "B.Sc (Data Science)")
        self.assertContains(response, "Student record updated successfully.")

    def test_student_delete_view_post(self):
        target_pk = self.student2.pk
        response = self.client.post(
            reverse('students:student_delete', kwargs={'pk': target_pk}),
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Student.objects.filter(pk=target_pk).exists())
        self.assertContains(response, "Student record deleted successfully.")


class StudentAdminTest(TestCase):
    def test_student_registered_in_admin(self):
        self.assertIn(Student, site._registry)
        admin_instance = site._registry[Student]
        self.assertIn('roll_number', admin_instance.list_display)
        self.assertIn('name', admin_instance.search_fields)
