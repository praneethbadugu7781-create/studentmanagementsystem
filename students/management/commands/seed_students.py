from django.core.management.base import BaseCommand
from students.models import Student


class Command(BaseCommand):
    help = 'Seeds student records matching the internship project demonstration slides.'

    def handle(self, *args, **kwargs):
        # Only seed initial sample data if database is currently empty
        if Student.objects.exists():
            self.stdout.write(
                self.style.NOTICE("Database already contains student records. Skipping seed.")
            )
            return
        
        sample_students = [
            {
                "name": "Akkala Naga Sarvani",
                "roll_number": "24CS001",
                "email": "sarvani@example.com",
                "course": "B.Sc Computer Science",
                "phone": "9876543210"
            },
            {
                "name": "Ravi Kumar",
                "roll_number": "24CS002",
                "email": "ravi@example.com",
                "course": "B.Sc Computer Science",
                "phone": "9876543211"
            },
            {
                "name": "Priya Sharma",
                "roll_number": "24CS003",
                "email": "priya@example.com",
                "course": "B.Sc Computer Science",
                "phone": "9876543212"
            },
            {
                "name": "Arjun Rao",
                "roll_number": "24CS004",
                "email": "arjun@example.com",
                "course": "B.Sc Computer Science",
                "phone": "9876543213"
            },
            {
                "name": "Kavya Reddy",
                "roll_number": "24CS005",
                "email": "kavya@example.com",
                "course": "B.Sc Computer Science",
                "phone": "9876543214"
            },
            {
                "name": "Sai Teja",
                "roll_number": "24CS006",
                "email": "saiteja@example.com",
                "course": "B.Sc Computer Science",
                "phone": "9876543215"
            },
        ]

        for data in sample_students:
            Student.objects.create(**data)

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully seeded {len(sample_students)} B.Sc Computer Science student records from internship demonstration."
            )
        )
