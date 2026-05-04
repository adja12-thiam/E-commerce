from django.shortcuts import render, get_object_or_404
from django.db.models import Sum, Count, Avg
from .models import Artisan, Produit, Categorie, Commande


def accueil(request):
    """Page d'accueil — hero + artisans vedettes + nouveautés"""
    artisans_vedettes = Artisan.objects.order_by('-note_moyenne')[:5]
    nouveaux_produits = Produit.objects.filter(est_actif=True, est_nouveau=True)[:6]

    stats = {
        'nb_artisans': Artisan.objects.count(),
        'nb_produits': Produit.objects.filter(est_actif=True).count(),
        'note_moy': Artisan.objects.aggregate(Avg('note_moyenne'))['note_moyenne__avg'] or 0,
    }

    context = {
        'artisans': artisans_vedettes,
        'produits': nouveaux_produits,
        'stats': stats,
    }
    return render(request, 'artisans/accueil.html', context)


def catalogue(request):
    """Page catalogue — recherche + filtres + grille"""
    produits = Produit.objects.filter(est_actif=True).select_related('artisan', 'categorie')
    categories = Categorie.objects.all()

    # Filtrage par catégorie
    cat_id = request.GET.get('categorie')
    if cat_id:
        produits = produits.filter(categorie__id=cat_id)

    # Recherche par nom ou artisan
    recherche = request.GET.get('q', '')
    if recherche:
        produits = produits.filter(nom__icontains=recherche) | \
                   produits.filter(artisan__nom__icontains=recherche)

    context = {
        'produits': produits,
        'categories': categories,
        'recherche': recherche,
        'cat_selectee': cat_id,
    }
    return render(request, 'artisans/catalogue.html', context)


def dashboard(request, artisan_id):
    """Tableau de bord de l'artisan"""
    artisan = get_object_or_404(Artisan, id=artisan_id)
    commandes = Commande.objects.filter(artisan=artisan).order_by('-date_commande')[:10]

    # Calcul des métriques
    ventes_mois = commandes.aggregate(total=Sum('prix_total'))['total'] or 0
    nb_commandes = commandes.count()
    nb_nouvelles = commandes.filter(statut='nouvelle').count()
    nb_produits = Produit.objects.filter(artisan=artisan, est_actif=True).count()

    context = {
        'artisan': artisan,
        'commandes': commandes,
        'ventes_mois': f"{ventes_mois:,}".replace(',', ' '),
        'nb_commandes': nb_commandes,
        'nb_nouvelles': nb_nouvelles,
        'nb_produits': nb_produits,
    }
    return render(request, 'artisans/dashboard.html', context)
