from enum import Enum

class MailTemplate(Enum):
    EXPIRES_30 = {
        "subject": "⏳ Vertrag läuft in 1 Monat ab – {{Produkt}}",
        "body": """Hallo 👋

        der folgende Vertrag nähert sich seinem Ablaufdatum:

        📄 Produkt: {{Produkt}}
        📅 Ablaufdatum: {{Ablaufdatum}}

        ⏳ Status: Läuft in 1 Monat ab

        👉 Empfehlung:
        Jetzt prüfen, ob der Vertrag verlängert oder gekündigt werden soll.

        – Automatische Vertragsüberwachung"""
    }

    EXPIRES_15 = {
        "subject": "⚠️ Noch 15 Tage – Vertrag {{Produkt}}",
        "body": """Hi,

        📄 Produkt: {{Produkt}}
        📅 Ablaufdatum: {{Ablaufdatum}}

        ⚠️ Status: Läuft in 15 Tagen ab

        👉 Jetzt ist ein guter Zeitpunkt für eine Entscheidung.

        – Automatische Vertragsüberwachung"""
    }

    EXPIRES_10 = {
        "subject": "⚠️ Noch 10 Tage – Vertrag {{Produkt}}",
        "body": """Hi,

        📄 Produkt: {{Produkt}}
        📅 Ablaufdatum: {{Ablaufdatum}}

        ⚠️ Status: Läuft in 10 Tagen ab

        👉 Jetzt ist ein guter Zeitpunkt für eine Entscheidung.

        – Automatische Vertragsüberwachung"""
    }

    EXPIRES_5 = {
        "subject": "⚠️ Noch 5 Tage – Vertrag {{Produkt}}",
        "body": """Hi,

        📄 Produkt: {{Produkt}}
        📅 Ablaufdatum: {{Ablaufdatum}}

        ⚠️ Status: Läuft in 5 Tagen ab

        👉 Jetzt ist ein guter Zeitpunkt für eine Entscheidung.

        – Automatische Vertragsüberwachung"""
    }

    EXPIRES_3 = {
        "subject": "⚠️ Noch 3 Tage – Vertrag {{Produkt}}",
        "body": """Hi,

        📄 Produkt: {{Produkt}}
        📅 Ablaufdatum: {{Ablaufdatum}}

        ⚠️ Status: Läuft in 3 Tagen ab

        👉 Jetzt ist ein guter Zeitpunkt für eine Entscheidung.

        – Automatische Vertragsüberwachung"""
    }

    EXPIRES_2 = {
        "subject": "⚠️ Noch 2 Tage – Vertrag {{Produkt}}",
        "body": """Hi,

        📄 Produkt: {{Produkt}}
        📅 Ablaufdatum: {{Ablaufdatum}}

        ⚠️ Status: Läuft in 2 Tagen ab

        👉 Jetzt ist ein guter Zeitpunkt für eine Entscheidung.

        – Automatische Vertragsüberwachung"""
    }

    EXPIRES_1 = {
        "subject": "⚠️ Noch 1 Tage – Vertrag {{Produkt}}",
        "body": """Hi,

        📄 Produkt: {{Produkt}}
        📅 Ablaufdatum: {{Ablaufdatum}}

        ⚠️ Status: Läuft in 1 Tagen ab

        👉 Jetzt ist ein guter Zeitpunkt für eine Entscheidung.

        – Automatische Vertragsüberwachung"""
    }

    EXPIRED = {
        "subject": "❌ Vertrag abgelaufen – {{Produkt}}",
        "body": """Info:

        📄 Produkt: {{Produkt}}
        📅 Ablaufdatum: {{Ablaufdatum}}

        ❌ Status: Abgelaufen

        👉 Falls notwendig, bitte manuell verlängern oder neu anlegen.

        – Automatische Vertragsüberwachung"""
    }