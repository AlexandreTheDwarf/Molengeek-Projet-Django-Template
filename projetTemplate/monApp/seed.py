from django_seed import Seed
from .models import Blog, Group, Portfolio, Contact
from faker import Faker
import random

def run():
    seeder = Seed.seeder()
    faker = Faker()

    # Génération des groupes (5 groupes)
    seeder.add_entity(Group, 5, {
        'name': lambda x: random.choice(["uiux", "branding", "identity", "illustrations"]),
    })

    # Génération des blogs (5 blogs)
    seeder.add_entity(Blog, 5, {
        'image': lambda x: f"img/portfolio-{random.randint(1, 5)}.jpg",
        'title': lambda x: faker.sentence(nb_words=6),
        'content': lambda x: faker.paragraph(nb_sentences=3),
        'url': lambda x: "blog-post.html",
    })

    # Génération des portfolios (5 portfolios)
    seeder.add_entity(Portfolio, 5, {
        'img': lambda x: f"img/portfolio-{random.randint(1, 10)}.jpg",
        'title': lambda x: faker.sentence(nb_words=4),
        'description': lambda x: faker.paragraph(nb_sentences=2),
    })

    seeder.add_entity(Contact, 1, {
        'title': lambda x: faker.sentence(nb_words=3),  
        'description': lambda x: faker.paragraph(nb_sentences=3),  
        'company': lambda x: faker.company(), 
        'phone': lambda x: faker.phone_number(),  
        'fax': lambda x: faker.phone_number(),  
        'email': lambda x: faker.email(), 
    })

    # Exécution des ajouts dans la base de données
    print("Données générées :")
    print(seeder.execute())

    # Après la création des portfolios, associer aléatoirement des groupes aux portfolios
    all_groups = list(Group.objects.all())
    for portfolio in Portfolio.objects.all():
        selected_groups = random.sample(all_groups, k=random.randint(1, 2))  # 1 à 2 groupes pour chaque portfolio
        portfolio.groups.set(selected_groups)

    print("Portfolios associés aux groupes.")
    print("🎉 Données de démo insérées avec succès !")
