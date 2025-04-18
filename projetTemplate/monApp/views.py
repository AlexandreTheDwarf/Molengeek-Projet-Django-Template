from django.shortcuts import render
from django.http import HttpResponse

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
    articles = [
        {
            "image": "img/portfolio-1.jpg",
            "title": "Is Passion Good For Business?",
            "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
            "url": "blog-post.html"
        },
        {
            "image": "img/portfolio-2.jpg",
            "title": "How to Stay Creative",
            "content": "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
            "url": "blog-post.html"
        },
    ]
    return render(request, "blog.html", {"articles": articles, "blog_intro" : blog_intro})

def contact(request):
    contact_info = {
        "title": "Get in touch",
        "description": "Just a note on how wonderful this theme is! If you are thinking of purchasing, i'd say do it! The flexibility is awesome possibilities are endless.",
        "company": "BusinessPerfect",
        "phone": "+1-541-754-3010",
        "fax": "+1-541-754-3010",
        "email": "hello@businessperfect.com"
    }
    return render(request, "contact.html", {"contact_info": contact_info})

def portfolio(request):
    projets = [
        {
            "img": "img/portfolio-1.jpg",
            "title": "Business Perfect item",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras viverra dolor eu nunc porttitor sollicitudin. Maecenas dignissim ultricies pharetra.",
            "groups": ["uiux"],
        },
        {
            "img": "img/portfolio-2.jpg",
            "title": "Business Perfect item",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras viverra dolor eu nunc porttitor sollicitudin. Maecenas dignissim ultricies pharetra.",
            "groups": ["branding"],
        },
        {
            "img": "img/portfolio-3.jpg",
            "title": "Business Perfect item",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras viverra dolor eu nunc porttitor sollicitudin. Maecenas dignissim ultricies pharetra.",
            "groups": ["identity"],
        },
        {
            "img": "img/portfolio-4.jpg",
            "title": "Business Perfect item",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras viverra dolor eu nunc porttitor sollicitudin. Maecenas dignissim ultricies pharetra.",
            "groups": ["uiux"],
        },
        {
            "img": "img/portfolio-5.jpg",
            "title": "Business Perfect item",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras viverra dolor eu nunc porttitor sollicitudin. Maecenas dignissim ultricies pharetra.",
            "groups": ["illustrations"],
        },
        {
            "img": "img/portfolio-6.jpg",
            "title": "Business Perfect item",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras viverra dolor eu nunc porttitor sollicitudin. Maecenas dignissim ultricies pharetra.",
            "groups": ["identity"],
        },
        {
            "img": "img/portfolio-7.jpg",
            "title": "Business Perfect item",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras viverra dolor eu nunc porttitor sollicitudin. Maecenas dignissim ultricies pharetra.",
            "groups": ["uiux"],
        },
        {
            "img": "img/portfolio-8.jpg",
            "title": "Business Perfect item",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras viverra dolor eu nunc porttitor sollicitudin. Maecenas dignissim ultricies pharetra.",
            "groups": ["branding"],
        },
        {
            "img": "img/portfolio-9.jpg",
            "title": "Business Perfect item",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras viverra dolor eu nunc porttitor sollicitudin. Maecenas dignissim ultricies pharetra.",
            "groups": ["uiux"],
        },
        {
            "img": "img/portfolio-10.jpg",
            "title": "Business Perfect item",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras viverra dolor eu nunc porttitor sollicitudin. Maecenas dignissim ultricies pharetra.",
            "groups": ["branding"],
        },
        {
            "img": "img/portfolio-2.jpg",
            "title": "Business Perfect item",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras viverra dolor eu nunc porttitor sollicitudin. Maecenas dignissim ultricies pharetra.",
            "groups": ["illustrations"],
        },
        {
            "img": "img/portfolio-9.jpg",
            "title": "Business Perfect item",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras viverra dolor eu nunc porttitor sollicitudin. Maecenas dignissim ultricies pharetra.",
            "groups": ["illustrations"],
        },
        {
            "img": "img/portfolio-5.jpg",
            "title": "Business Perfect item",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras viverra dolor eu nunc porttitor sollicitudin. Maecenas dignissim ultricies pharetra.",
            "groups": ["identity"],
        },
        {
            "img": "img/portfolio-6.jpg",
            "title": "Business Perfect item",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras viverra dolor eu nunc porttitor sollicitudin. Maecenas dignissim ultricies pharetra.",
            "groups": ["branding"],
        },
        {
            "img": "img/portfolio-3.jpg",
            "title": "Business Perfect item",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras viverra dolor eu nunc porttitor sollicitudin. Maecenas dignissim ultricies pharetra.",
            "groups": ["illustrations"],
        },
    ]
    return render(request, "portfolio.html", {'projets': projets})