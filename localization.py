translations = {
    'en': {
        "just now": "just now",
        "less than a minute ago": "less than a minute ago",
        "couple of minutes ago": "couple of minutes ago",
        "hour ago": "hour ago",
        "today": "today",
        "yesterday": "yesterday",
        "this week": "this week",
        "long time ago": "long time ago",
        "Never": "Never"
    },
    'uk': {
        "just now": "щойно",
        "less than a minute ago": "менше хвилини тому",
        "couple of minutes ago": "кілька хвилин тому",
        "hour ago": "годину тому",
        "today": "сьогодні",
        "yesterday": "вчора",
        "this week": "цього тижня",
        "long time ago": "давно",
        "Never": "Ніколи"
    },
    'ar': {
        "just now": "الآن",
        "less than a minute ago": "قبل دقيقة أو أقل",
        "couple of minutes ago": "قبل بضع دقائق",
        "hour ago": "قبل ساعة",
        "today": "اليوم",
        "yesterday": "أمس",
        "this week": "هذا الأسبوع",
        "long time ago": "منذ وقت طويل",
        "Never": "أبدًا"
    },
    'fr': {
        "just now": "à l'instant",
        "less than a minute ago": "il y a moins d'une minute",
        "couple of minutes ago": "il y a quelques minutes",
        "hour ago": "il y a une heure",
        "today": "aujourd'hui",
        "yesterday": "hier",
        "this week": "cette semaine",
        "long time ago": "il y a longtemps",
        "Never": "Jamais"
    }
}

def translate(text, lang):
    """Translate the given text to the specified language."""
    return translations.get(lang, {}).get(text, text)

# Example usage:
# print(translate("just now", "uk"))  # Outputs: щойно
