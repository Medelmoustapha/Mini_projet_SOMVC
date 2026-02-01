class Observateur:
    def update(self, compte):
        pass

class CompteBancaire:
    __instance = None

    def __new__(cls, titulaire, solde_initial=0):
        if cls.__instance is None:
            cls.__instance = super(CompteBancaire, cls).__new__(cls)
            cls.__instance.titulaire = titulaire
            cls.__instance.solde = solde_initial
            cls.__instance.historique = []
            cls.__instance.observateurs = []
        return cls.__instance

    def ajouter_observateur(self, obs):
        self.observateurs.append(obs)

    def notifier(self):
        for obs in self.observateurs:
            obs.update(self)

    def depot(self, montant):
        self.solde += montant
        self.historique.append(f"Dépôt : +{montant}")
        self.notifier()

    def retrait(self, montant):
        self.solde -= montant
        self.historique.append(f"Retrait : -{montant}")
        self.notifier()

class VueAffichageSolde(Observateur):
    def update(self, compte):
        print("Solde actuel :", compte.solde)

class VueHistoriqueOperations(Observateur):
    def update(self, compte):
        print("Historique des opérations :")
        for op in compte.historique:
            print("-", op)

class VueAlerteSolde(Observateur):
    def update(self, compte):
        if compte.solde < 0:
            print("ALERTE : Solde négatif !")

class CompteController:
    def __init__(self, compte):
        self.compte = compte

    def effectuer_depot(self, montant):
        self.compte.depot(montant)

    def effectuer_retrait(self, montant):
        if self.compte.solde - montant < -500:
            print("Retrait refusé : plafond dépassé")
        else:
            self.compte.retrait(montant)

compte = CompteBancaire("Ahmed", 100)

vue_solde = VueAffichageSolde()
vue_hist = VueHistoriqueOperations()
vue_alerte = VueAlerteSolde()

compte.ajouter_observateur(vue_solde)
compte.ajouter_observateur(vue_hist)
compte.ajouter_observateur(vue_alerte)

controller = CompteController(compte)

controller.effectuer_depot(50)
print("-----")
controller.effectuer_retrait(200)
print("-----")
controller.effectuer_retrait(500)
