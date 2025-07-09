from django.core.management.base import BaseCommand
from jobRecord.models import Candidate, Skill, Industry
import random

class Command(BaseCommand):
    help = 'Remplit la base avec des candidats, compétences et industries fictives'

    def handle(self, *args, **kwargs):
        # 1. Création de quelques industries
        industries = ['Tech', 'Finance', 'Healthcare', 'Education']
        industry_objs = []
        for name in industries:
            obj, created = Industry.objects.get_or_create(name=name)
            industry_objs.append(obj)
        self.stdout.write(f"Industries créées : {[i.name for i in industry_objs]}")

        # 2. Création de quelques compétences
        skills = ['Python', 'Django', 'JavaScript', 'React', 'SQL']
        skill_objs = []
        for name in skills:
            obj, created = Skill.objects.get_or_create(name=name)
            skill_objs.append(obj)
        self.stdout.write(f"Skills créés : {[s.name for s in skill_objs]}")

        # 3. Création de candidats
        candidates_data = [
            {'name': 'Alice Dupont', 'email': 'alice@example.com', 'location': 'Paris'},
            {'name': 'Bob Martin', 'email': 'bob@example.com', 'location': 'Lyon'},
            {'name': 'Claire Dubois', 'email': 'claire@example.com', 'location': 'Marseille'},
        ]

        for data in candidates_data:
            industry = random.choice(industry_objs)
            candidate, created = Candidate.objects.get_or_create(
                email=data['email'],
                defaults={
                    'name': data['name'],
                    'location': data['location'],
                    'industry': industry,
                }
            )
            if created:
                # Ajout de 2 compétences aléatoires
                candidate.skills.set(random.sample(skill_objs, 2))
                self.stdout.write(self.style.SUCCESS(f"Candidat créé : {candidate.name}"))
            else:
                self.stdout.write(self.style.WARNING(f"Candidat déjà existant : {candidate.name}"))
