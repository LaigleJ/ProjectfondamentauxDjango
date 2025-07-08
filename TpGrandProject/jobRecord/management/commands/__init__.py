import csv
from django.core.management.base import BaseCommand
from jobRecord.models import JobRecord, Contract, Industry, Candidate  # adapte si tu changes de noms

class Command(BaseCommand):
    help = 'Import job records from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Chemin vers le fichier CSV à importer')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        with open(csv_file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                contract_type, _ = Contract.objects.get_or_create(type_code=row['employment_type'], defaults={'description': row['employment_type']})
                industry_obj, _ = Industry.objects.get_or_create(name="Unknown")  # Optionnel
                candidate_obj, _ = Candidate.objects.get_or_create(name="Anonymous", email="anon@example.com", location="Unknown")

                JobRecord.objects.create(
                    work_year=int(row['work_year']),
                    experience_level=row['experience_level'],
                    employment_type=contract_type,
                    job_title=row['job_title'],
                    salary=row['salary'],
                    salary_currency=row['salary_currency'],
                    salary_in_usd=row['salary_in_usd'],
                    employee_residence=row['employee_residence'],
                    remote_ratio=int(row['remote_ratio']),
                    company_location=row['company_location'],
                    company_size=row['company_size'],
                    industry=industry_obj,
                    candidate=candidate_obj,
                )

        self.stdout.write(self.style.SUCCESS('✅ Données importées avec succès !'))
