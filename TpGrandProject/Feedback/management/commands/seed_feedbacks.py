from django.core.management.base import BaseCommand
from Feedback.models import Feedback  # adapte si l'app s'appelle différemment
from jobRecord.models import JobRecord, Candidate
import random

class Command(BaseCommand):
    help = 'Génère des feedbacks fictifs pour les JobRecords existants'

    def handle(self, *args, **kwargs):
        comments = [
            "Excellent travail, rien à redire.",
            "Quelques points à améliorer, mais globalement bon.",
            "Résultats décevants par rapport aux attentes.",
            "Très bon esprit d'équipe et autonomie.",
            "Manque de rigueur sur certains aspects techniques."
        ]

        jobs = JobRecord.objects.all()
        candidates = list(Candidate.objects.all())

        if not jobs.exists():
            self.stdout.write(self.style.WARNING("Aucun JobRecord trouvé."))
            return

        for job in jobs:
            nb_feedbacks = random.randint(1, 3)
            for _ in range(nb_feedbacks):
                comment = random.choice(comments)
                rating = random.randint(1, 5)
                author = random.choice(candidates) if candidates else None

                Feedback.objects.create(
                    job=job,
                    author=author,
                    comment=comment,
                    rating=rating
                )

            self.stdout.write(self.style.SUCCESS(
                f"{nb_feedbacks} feedback(s) ajouté(s) pour le job {job.job_title} ({job.id})"
            ))
