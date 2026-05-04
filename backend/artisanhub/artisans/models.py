from django.db import models


class Artisan(models.Model):
    nom = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='artisans/', blank=True, null=True)
    bio = models.TextField(blank=True)
    note_moyenne = models.FloatField(default=0)
    ventes_mois = models.IntegerField(default=0)
    date_inscription = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom


class Categorie(models.Model):
    nom = models.CharField(max_length=50)
    icone = models.CharField(max_length=10, default='🛍')

    def __str__(self):
        return self.nom


class Produit(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    prix = models.IntegerField()  # en Francs CFA
    image = models.ImageField(upload_to='produits/', blank=True, null=True)
    icone = models.CharField(max_length=10, default='📦')
    artisan = models.ForeignKey(Artisan, on_delete=models.CASCADE, related_name='produits')
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True, blank=True)
    note = models.FloatField(default=0)
    est_nouveau = models.BooleanField(default=False)
    est_actif = models.BooleanField(default=True)
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom

    def prix_formate(self):
        return f"{self.prix:,} F".replace(',', ' ')


class Commande(models.Model):
    STATUT_CHOICES = [
        ('nouvelle', 'Nouvelle'),
        ('en_cours', 'En cours'),
        ('livree', 'Livrée'),
        ('annulee', 'Annulée'),
    ]
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    artisan = models.ForeignKey(Artisan, on_delete=models.CASCADE)
    client_nom = models.CharField(max_length=100)
    quantite = models.IntegerField(default=1)
    prix_total = models.IntegerField()
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='nouvelle')
    date_commande = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commande #{self.id} - {self.client_nom}"

    def prix_total_formate(self):
        return f"{self.prix_total:,} F".replace(',', ' ')
