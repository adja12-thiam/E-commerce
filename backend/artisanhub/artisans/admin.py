from django.contrib import admin
from .models import Artisan, Produit, Categorie, Commande

admin.site.register(Artisan)
admin.site.register(Produit)
admin.site.register(Categorie)
admin.site.register(Commande)
