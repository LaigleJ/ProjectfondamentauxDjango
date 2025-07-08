from django.core.management.base import BaseCommand
from jobRecord.models import JobRecord
from django.db.models import Avg, Count
import os

class Command(BaseCommand):
    help = "Analyse les données de JobRecord et les enregistre dans un fichier texte"

    def handle(self, *args, **kwargs):
        output = []

        # 1. Top 5 des jobs les mieux payés
        top_jobs = JobRecord.objects.order_by('-salary_in_usd')[:5]
        output.append("Top 5 jobs les mieux payés en USD :")
        for job in top_jobs:
            output.append(f"{job.job_title} - {job.salary_in_usd} USD")
        output.append("")

        # 2. Salaire moyen par niveau d'expérience
        output.append("Salaire moyen par niveau d'expérience :")
        avg_salaries = JobRecord.objects.values('experience_level').annotate(avg_salary=Avg('salary_in_usd'))
        for row in avg_salaries:
            output.append(f"{row['experience_level']} : {round(row['avg_salary'], 2)} USD")
        output.append("")

        # 3. Nombre de jobs par location
        output.append("Nombre de jobs par company_location :")
        location_counts = JobRecord.objects.values('company_location').annotate(total=Count('id')).order_by('-total')
        for row in location_counts:
            output.append(f"{row['company_location']} : {row['total']}")
        output.append("")

        # 4. Ratio des jobs 100% remote
        total_jobs = JobRecord.objects.count()
        remote_jobs = JobRecord.objects.filter(remote_ratio=100).count()
        remote_ratio = (remote_jobs / total_jobs) * 100 if total_jobs > 0 else 0
        output.append(f"Ratio des jobs 100% remote : {round(remote_ratio, 2)}%")
        output.append("")

        # 5. Écriture dans un fichier texte
        results_path = os.path.join("data", "results.txt")
        with open(results_path, "w", encoding="utf-8") as f:
            for line in output:
                f.write(line + "\n")

        # Affichage en console
        for line in output:
            self.stdout.write(line)
