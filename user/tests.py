from django.test import TestCase
from django.urls import reverse
from .models import Student
from .forms import StudentForm
import datetime

class StudentModelTests(TestCase):
    def test_student_creation(self):
        student = Student.objects.create(
            first_name="Jane",
            last_name="Smith",
            roll_number="STU2002",
            email="jane.smith@example.com",
            mobile_no="0987654321",
            date_of_birth=datetime.date(2005, 5, 20),
            gender="Female",
            class_name="Grade 11",
            marks=88.50,
            address="456 Oak St"
        )
        self.assertEqual(str(student), "Jane Smith (STU2002)")
        self.assertEqual(student.first_name, "Jane")

class StudentFormTests(TestCase):
    def test_valid_form(self):
        form_data = {
            'first_name': 'Alex',
            'last_name': 'Jones',
            'roll_number': 'STU3003',
            'email': 'alex.jones@example.com',
            'mobile_no': '5551234567',
            'date_of_birth': '2006-03-15',
            'gender': 'Male',
            'class_name': 'Grade 10',
            'marks': 75.00,
            'address': '789 Pine St'
        }
        form = StudentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_marks_form(self):
        form_data = {
            'first_name': 'Alex',
            'last_name': 'Jones',
            'roll_number': 'STU3003',
            'email': 'alex.jones@example.com',
            'mobile_no': '5551234567',
            'date_of_birth': '2006-03-15',
            'gender': 'Male',
            'class_name': 'Grade 10',
            'marks': 105.00,  # invalid max is 100
            'address': '789 Pine St'
        }
        form = StudentForm(data=form_data)
        self.assertFalse(form.is_valid())

class StudentViewsTests(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            first_name="John",
            last_name="Doe",
            roll_number="STU1001",
            email="john.doe@example.com",
            mobile_no="1234567890",
            date_of_birth=datetime.date(2004, 10, 10),
            gender="Male",
            class_name="Grade 12",
            marks=92.50,
            address="123 Main St"
        )

    def test_student_list_view(self):
        response = self.client.get(reverse('student_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "John Doe")

    def test_student_detail_view(self):
        response = self.client.get(reverse('student_detail', kwargs={'pk': self.student.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "john.doe@example.com")

    def test_student_create_post(self):
        post_data = {
            'first_name': 'Bobby',
            'last_name': 'Brown',
            'roll_number': 'STU4004',
            'email': 'bobby.brown@example.com',
            'mobile_no': '5559876543',
            'date_of_birth': '2005-09-09',
            'gender': 'Male',
            'class_name': 'Grade 11',
            'marks': 65.00,
            'address': '321 Maple Ave'
        }
        response = self.client.post(reverse('student_create'), data=post_data)
        self.assertEqual(response.status_code, 302)  # Redirects to list
        self.assertTrue(Student.objects.filter(roll_number='STU4004').exists())

