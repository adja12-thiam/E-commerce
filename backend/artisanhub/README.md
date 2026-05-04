# ArtisanHub — Guide d'installation Django

## Structure du projet

```
artisanhub/
├── manage.py
├── artisanhub/               ← configuration du projet
│   ├── settings.py
│   └── urls.py
└── artisans/                 ← application principale
    ├── models.py             ← Artisan, Produit, Categorie, Commande
    ├── views.py              ← accueil, catalogue, dashboard
    ├── urls.py               ← routes
    ├── admin.py              ← interface admin
    ├── templates/artisans/
    │   ├── base.html         ← nav + bottom bar partagés
    │   ├── accueil.html
    │   ├── catalogue.html
    │   └── dashboard.html
    └── static/artisans/
        ├── css/style.css
        └── js/main.js
```

## Installation

```bash
# 1. Installer Django
pip install django pillow

# 2. Se placer dans le dossier
cd artisanhub

# 3. Créer la base de données
python manage.py makemigrations
python manage.py migrate

# 4. Créer un compte admin
python manage.py createsuperuser

# 5. Lancer le serveur
python manage.py runserver
```

## Accès

- Site : http://127.0.0.1:8000/
- Catalogue : http://127.0.0.1:8000/catalogue/
- Dashboard : http://127.0.0.1:8000/dashboard/1/
- Admin : http://127.0.0.1:8000/admin/

## Ajouter des données (via admin)

1. Aller sur http://127.0.0.1:8000/admin/
2. Créer des Catégories (Poterie, Bijoux...)
3. Créer des Artisans
4. Créer des Produits liés aux artisans

## Connexion avec le Back-end (équipe)

Le Back-end doit fournir les données via les modèles Django.
Tout passe par `views.py` qui récupère les données et les
envoie aux templates avec `render(request, template, context)`.
