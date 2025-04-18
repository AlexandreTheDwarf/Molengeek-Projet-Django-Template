## 📁 Django BusinessPerfect - Template Integration

Ce projet est une intégration du thème **BusinessPerfect** dans un projet Django. Il sert de base pour les prochains chapitres du cours, donc une bonne intégration ici est essentielle pour la suite.

---

### 🧱 Objectif

Intégrer proprement un template HTML statique dans un projet Django, en utilisant :
- Les **templates Django** (`base.html`, `index.html`, etc.)
- Le **système de variables contextuelles** (données dynamiques depuis la vue)
- Les **boucles** dans les templates pour éviter les répétitions
- Le **tag `{% static %}`** pour les ressources (images, CSS, JS...)

---

### 🔧 Structure des fichiers

```
project/
│
├── myapp/
│   ├── views.py          # Contient les variables envoyées aux templates
│   ├── templates/
│   │   ├── base.html     # Template de base (header, footer, etc.)
│   │   └── index.html    # Page d'accueil intégrée
│   └── static/
│       └── img/          # Contient les images comme we-are-creative.jpg
│
└── manage.py
```

---

### 🖼️ Template intégrée

Pages intégrées avec variables :

| Section                | Variables utilisées                       |
|------------------------|-------------------------------------------|
| Hero                  | `hero_text`                                |
| Citation              | `quote_text`, `quote_author`               |
| Section "We Are Creative" | `creative_title`, `creative_description`, `creative_img` |
| Section "We Are The Best" | `best_title`, `best_description`       |
| Services              | `services` (liste de dictionnaires)        |
| Call to Action        | `team_motto`                               |

---

### 🌀 Exemple de boucle pour les services

**Vue (views.py)**

```python
services = [
    {"icon": "fa-laptop", "title": "Clean Design", "description": "..."},
    {"icon": "fa-wrench", "title": "Customizable", "description": "..."},
    # etc.
]
```

**Template (index.html)**

```django
{% for service in services %}
<div class="service">
    <div class="service-icon">
        <i class="fa {{ service.icon }}" aria-hidden="true"></i>
    </div>
    <div class="service-content">
        <h4 class="service-title">{{ service.title }}</h4>
        <p>{{ service.description }}</p>
    </div>
</div>
{% endfor %}
```

---

### ✅ Bonnes pratiques respectées

- Utilisation des **blocs (`{% block content %}`)** dans `base.html`
- Utilisation de **`{% static %}`** sans erreurs de syntaxe
- Séparation claire entre **logique (views.py)** et **affichage (templates)**
- Utilisation des **contextes** pour éviter le contenu en dur

---

### 🚀 Lancer le projet

```bash
# Installation
pip install django

# Lancer le serveur
python manage.py runserver
```

Accédez à `http://127.0.0.1:8000/` pour voir la page d'accueil avec le thème intégré.
