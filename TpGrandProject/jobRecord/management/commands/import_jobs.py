import csv
from django.core.management.base import BaseCommand
from jobRecord.models import Contract, Industry, Candidate, JobRecord

class Command(BaseCommand):
    help = "Import jobs from a CSV file"

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Chemin vers le fichier CSV')

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        created_count = 0

        with open(csv_file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Contrat (employment_type)
                contract, _ = Contract.objects.get_or_create(
                    type_code=row['employment_type'],
                    defaults={'description': row.get('employment_type', '')}
                )

                # Industrie
                industry = None
                industry_name = row.get('industry')
                if industry_name:
                    industry, _ = Industry.objects.get_or_create(name=industry_name)

                # Candidate (exemple simplifié : on crée un candidat avec juste un email unique)
                candidate_email = row.get('candidate_email')
                candidate = None
                if candidate_email:
                    candidate, _ = Candidate.objects.get_or_create(email=candidate_email, defaults={
                        'name': row.get('candidate_name', 'Unknown'),
                        'location': row.get('employee_residence', '')
                    })

                # Vérification doublons
                exists = JobRecord.objects.filter(
                    job_title=row['job_title'],
                    work_year=int(row['work_year']),
                    employee_residence=row['employee_residence'],
                    company_location=row['company_location'],
                ).exists()

                if not exists:
                    JobRecord.objects.create(
                        work_year=int(row['work_year']),
                        experience_level=row['experience_level'],
                        employment_type=contract,
                        job_title=row['job_title'],
                        salary=float(row['salary']),
                        salary_currency=row['salary_currency'],
                        salary_in_usd=float(row['salary_in_usd']),
                        employee_residence=row['employee_residence'],
                        remote_ratio=int(row['remote_ratio']),
                        company_location=row['company_location'],
                        company_size=row['company_size'],
                        industry=industry,
                        candidate=candidate,
                    )
                    created_count += 1

        self.stdout.write(self.style.SUCCESS(f"{created_count} JobRecord(s) créés."))
