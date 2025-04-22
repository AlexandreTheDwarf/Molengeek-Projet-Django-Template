from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog
from .models import Portfolio
from .models import Group
from .models import Contact

# Create your views here.

def index(request):
    context = {
        "hero_text": "Simplicity is the soul of efficiency",
        "quote_text": "I owe my success to having listened respectfully to the very best advice, and then going away and doing the exact opposite",
        "quote_author": "G. K. Chesterton",
        "creative_img": "img/we-are-creative.jpg",
        "creative_img_desc": "We are creative",
        "creative_title": "We Are Creative",
        "creative_description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam et nunc nunc. Ut consectetur felis sit amet fermentum accumsan.",
        "best_title": "We Are The Best",
        "best_description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "team_motto": "Coming together is a beginning, keeping together is progress, working together is success.",
        "services": [
            {
                "icon": "fa-laptop",
                "title": "Clean Design",
                "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor",
            },
            {
                "icon": "fa-wrench",
                "title": "Customizable",
                "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor",
            },
            {
                "icon": "fa-arrows-alt",
                "title": "Responsive Layout",
                "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor",
            },
            {
                "icon": "fa-cogs",
                "title": "Multi-Purpose",
                "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor",
            },
        ]
    }
    return render(request, "index.html", context)

def blog(request):
    blog_intro = "Découvrez nos derniers articles, pensées et idées sur le développement, le design et plus encore."
    articles = Blog.objects.all()  # récupération des articles depuis la DB
    return render(request, "blog.html", {"articles": articles, "blog_intro": blog_intro})

def contact(request):
    contact_info = Contact.objects.first()  
    return render(request, "contact.html", {'contact_info': contact_info})

def portfolio(request):
    # Récupère tous les projets Portfolio dans la base de données
    projets = Portfolio.objects.all()

    # Prépare une liste des projets avec leurs groupes associés
    projets_data = []
    for projet in projets:
        projets_data.append({
            "img": projet.img,
            "title": projet.title,
            "description": projet.description,
            "groups": [group.name for group in projet.groups.all()],
        })

    return render(request, "portfolio.html", {'projets': projets_data})