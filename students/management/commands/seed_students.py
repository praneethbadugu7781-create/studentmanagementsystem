from django.core.management.base import BaseCommand
from students.models import Student


class Command(BaseCommand):
    help = 'Seeds exactly 40 student records for B.Sc (Computer Science) with realistic student names.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--reset',
            action='store_true',
            help='Deletes all existing student records and seeds 40 fresh B.Sc (Computer Science) students.',
        )

    def handle(self, *args, **options):
        reset = options.get('reset', False)

        if reset:
            deleted_count, _ = Student.objects.all().delete()
            self.stdout.write(self.style.WARNING(f"Cleared {deleted_count} existing records."))
        elif Student.objects.exists():
            self.stdout.write(
                self.style.NOTICE("Database already contains student records. Use --reset to replace with 40 fresh students.")
            )
            return

        sample_students = [
            {"name": "Akkala Naga Sarvani", "roll_number": "24CS001", "email": "sarvani.akkala@example.com", "course": "B.Sc (Computer Science)", "phone": "9876543210"},
            {"name": "Bonda Sai Teja", "roll_number": "24CS002", "email": "saiteja.bonda@example.com", "course": "B.Sc (Computer Science)", "phone": "9876543211"},
            {"name": "Chunduru Priya", "roll_number": "24CS003", "email": "priya.chunduru@example.com", "course": "B.Sc (Computer Science)", "phone": "9876543212"},
            {"name": "Daggubati Rahul", "roll_number": "24CS004", "email": "rahul.daggubati@example.com", "course": "B.Sc (Computer Science)", "phone": "9876543213"},
            {"name": "Goli Kavya", "roll_number": "24CS005", "email": "kavya.goli@example.com", "course": "B.Sc (Computer Science)", "phone": "9876543214"},
            {"name": "Jampana Arjun", "roll_number": "24CS006", "email": "arjun.jampana@example.com", "course": "B.Sc (Computer Science)", "phone": "9876543215"},
            {"name": "Kakarla Sneha", "roll_number": "24CS007", "email": "sneha.kakarla@example.com", "course": "B.Sc (Computer Science)", "phone": "9876543216"},
            {"name": "Mandava Rohit", "roll_number": "24CS008", "email": "rohit.mandava@example.com", "course": "B.Sc (Computer Science)", "phone": "9876543217"},
            {"name": "Nallamothu Ananya", "roll_number": "24CS009", "email": "ananya.nallamothu@example.com", "course": "B.Sc (Computer Science)", "phone": "9876543218"},
            {"name": "Pamidighantam Varun", "roll_number": "24CS010", "email": "varun.p@example.com", "course": "B.Sc (Computer Science)", "phone": "9876543219"},
            {"name": "Rayapati Harika", "roll_number": "24CS011", "email": "harika.rayapati@example.com", "course": "B.Sc (Computer Science)", "phone": "9876543220"},
            {"name": "Sunkara Karthik", "roll_number": "24CS012", "email": "karthik.sunkara@example.com", "course": "B.Sc (Computer Science)", "phone": "9876543221"},
            {"name": "Talluri Deepthi", "roll_number": "24CS013", "email": "deepthi.talluri@example.com", "course": "B.Sc (Computer Science)", "phone": "9876543222"},
            {"name": "Vuyyuru Naveen", "roll_number": "24CS014", "email": "naveen.vuyyuru@example.com", "course": "B.Sc (Computer Science)", "phone": "9876543223"},
            {"name": "Yalamanchili Pooja", "roll_number": "24CS015", "email": "pooja.yalamanchili@example.com", "course": "B.Sc (Computer Science)", "phone": "9876543224"},
            {"name": "Alluri Tarun", "roll_number": "24CS016", "email": "tarun.alluri@example.com", "course": "B.Sc (Computer Science)", "phone": "9876543225"},
            {"name": "Bandi Meghana", "roll_number": "24CS017", "email": "meghana.bandi@example.com", "course": "B.Sc (Computer Science)", "phone": "9876543226"},
            {"name": "Chebrolu Aditya", "roll_number": "24CS018", "email": "aditya.chebrolu@example.com", "course": "B.Sc (Computer Science)", "phone": "9876543227"},
            {"name": "Dasari Divya", "roll_number": "24CS019", "email": "divya.dasari@example.com", "course": "B.Sc (Computer Science)", "phone": "9876543228"},
            {"name": "Guntupalli Manoj", "roll_number": "24CS020", "email": "manoj.guntupalli@example.com", "course": "B.Sc (Computer Science)", "phone": "9876543229"},
            {"name": "Indukuri Swetha", "roll_number": "24CS021", "email": "swetha.indukuri@example.com", "course": "B.Sc (Computer Science)", "phone": "9876543230"},
            {"name": "Jonnalagadda Suresh", "roll_number": "24CS022", "email": "suresh.j@example.com", "course": "B.Sc (Computer Science)", "phone": "9876543231"},
            {"name": "Kanumuri Yamini", "roll_number": "24CS023", "email": "yamini.kanumuri@example.com", "course": "B.Sc (Computer Science)", "phone": "9876543232"},
            {"name": "Lingamaneni Lokesh", "roll_number": "24CS024", "email": "lokesh.l@example.com", "course": "B.Sc (Computer Science)", "phone": "9876543233"},
            {"name": "Mulpuri Bhavana", "roll_number": "24CS025", "email": "bhavana.mulpuri@example.com", "course": "B.Sc (Computer Science)", "phone": "9876543234"},
            {"name": "Nadendla Charan", "roll_number": "24CS026", "email": "charan.nadendla@example.com", "course": "B.Sc (Computer Science)", "phone": "9876543235"},
            {"name": "Paruchuri Ramya", "roll_number": "24CS027", "email": "ramya.paruchuri@example.com", "course": "B.Sc (Computer Science)", "phone": "9876543236"},
            {"name": "Ravipati Kalyan", "roll_number": "24CS028", "email": "kalyan.ravipati@example.com", "course": "B.Sc (Computer Science)", "phone": "9876543237"},
            {"name": "Surapaneni Aravind", "roll_number": "24CS029", "email": "aravind.s@example.com", "course": "B.Sc (Computer Science)", "phone": "9876543238"},
            {"name": "Tummala Sireesha", "roll_number": "24CS030", "email": "sireesha.tummala@example.com", "course": "B.Sc (Computer Science)", "phone": "9876543239"},
            {"name": "Vadlamudi Ganesh", "roll_number": "24CS031", "email": "ganesh.vadlamudi@example.com", "course": "B.Sc (Computer Science)", "phone": "9876543240"},
            {"name": "Velagapudi Pranavi", "roll_number": "24CS032", "email": "pranavi.velagapudi@example.com", "course": "B.Sc (Computer Science)", "phone": "9876543241"},
            {"name": "Yaralagadda Vignesh", "roll_number": "24CS033", "email": "vignesh.y@example.com", "course": "B.Sc (Computer Science)", "phone": "9876543242"},
            {"name": "Atluri Keerthana", "roll_number": "24CS034", "email": "keerthana.atluri@example.com", "course": "B.Sc (Computer Science)", "phone": "9876543243"},
            {"name": "Boddepalli Vivek", "roll_number": "24CS035", "email": "vivek.boddepalli@example.com", "course": "B.Sc (Computer Science)", "phone": "9876543244"},
            {"name": "Chalasani Lavanya", "roll_number": "24CS036", "email": "lavanya.chalasani@example.com", "course": "B.Sc (Computer Science)", "phone": "9876543245"},
            {"name": "Duvvuri Pradeep", "roll_number": "24CS037", "email": "pradeep.duvvuri@example.com", "course": "B.Sc (Computer Science)", "phone": "9876543246"},
            {"name": "Gorantla Tejaswini", "roll_number": "24CS038", "email": "tejaswini.gorantla@example.com", "course": "B.Sc (Computer Science)", "phone": "9876543247"},
            {"name": "Jagarlamudi Harish", "roll_number": "24CS039", "email": "harish.j@example.com", "course": "B.Sc (Computer Science)", "phone": "9876543248"},
            {"name": "Kondragunta Sandhya", "roll_number": "24CS040", "email": "sandhya.kondragunta@example.com", "course": "B.Sc (Computer Science)", "phone": "9876543249"},
        ]

        for data in sample_students:
            Student.objects.create(**data)

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully seeded {len(sample_students)} student records strictly for B.Sc (Computer Science)."
            )
        )
