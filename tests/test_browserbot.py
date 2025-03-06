# tests/test_browserbot.py
from autoflow.core import BrowserBot

def test_browserbot_initialization():
    """Teste si BrowserBot s'initialise correctement."""
    bot = BrowserBot(browser="chrome")
    assert bot.driver is not None, "Le driver Chrome n'a pas été initialisé"
    bot.close()