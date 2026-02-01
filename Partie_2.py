class CompteBancaire:
    __instance = None

    def __new__(cls, solde_initial=0):
        if cls.__instance is None:
            cls.__instance = super(CompteBancaire, cls).__new__(cls)
            cls.__instance.solde = solde_initial
            cls.__instance.historique = []
        return cls.__instance

    def depot(self, montant):
        self.solde += montant
        self.historique.append(f"Dépôt : +{montant}")

    def retrait(self, montant):
        self.solde -= montant
        self.historique.append(f"Retrait : -{montant}")

class AffichageSolde:
    def afficher(self, compte):
        print("Solde actuel :", compte.solde)

class HistoriqueOperations:
    def afficher(self, compte):
        print("Historique des opérations :")
        for op in compte.historique:
            print(op)

class AlerteSolde:
    def verifier(self, compte):
        if compte.solde < 0:
            print("ALERTE : Solde négatif !")

class ControleOperations:
    def verifier(self, compte):
        if compte.solde < -500:
            print("Découvert excessif !")


compte1 = CompteBancaire(100)
compte2 = CompteBancaire(500)

affichage = AffichageSolde()
historique = HistoriqueOperations()
alerte = AlerteSolde()
controle = ControleOperations()

compte1.depot(50)
affichage.afficher(compte2)
historique.afficher(compte2)

print("-----")

compte2.retrait(200)
affichage.afficher(compte1)
historique.afficher(compte1)
alerte.verifier(compte1)
controle.verifier(compte1)
