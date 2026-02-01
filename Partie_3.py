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

class Observateur:
    def update(self, compte):
        pass

class AffichageSolde(Observateur):
    def update(self, compte):
        print("Solde :", compte.solde)

class HistoriqueOperations(Observateur):
    def update(self, compte):
        print("Historique des opérations :")
        for op in compte.historique:
            print("-", op)

class AlerteSolde(Observateur):
    def update(self, compte):
        if compte.solde < 0:
            print("ALERTE : Solde négatif !")

class ControleOperations(Observateur):
    def update(self, compte):
        if compte.solde < -500:
            print("Découvert excessif !")


compte = CompteBancaire("Ahmed", 100)

m1 = AffichageSolde()
m2 = HistoriqueOperations()
m3 = AlerteSolde()
m4 = ControleOperations()

compte.ajouter_observateur(m1)
compte.ajouter_observateur(m2)
compte.ajouter_observateur(m3)
compte.ajouter_observateur(m4)

compte.depot(50)
print("-----")
compte.retrait(200)
print("-----")
compte.retrait(500)
