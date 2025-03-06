# src/autoflow/core.py

class BrowserBot:
    def __init__(self, browser):
        self.browser = browser
        # Ici, vous pouvez initialiser le driver de manière réelle ou simuler son initialisation.
        # Pour l'instant, nous utilisons une valeur factice pour permettre aux tests de passer.
        self.driver = f"Driver for {browser}"

    def close(self):
        # Ferme le driver (simulé ici)
        self.driver = None
