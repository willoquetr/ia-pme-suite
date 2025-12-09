import json


# Templates d'emails customisables par catégorie
EMAIL_TEMPLATES = {
    "invoice": {
        "default": """Dear Client,

Thank you for your recent invoice inquiry. We have processed your request and the details are as follows:

[INSERT INVOICE DETAILS HERE]

Please review and confirm receipt. If you have any questions, please don't hesitate to contact us.

Best regards,
[YOUR NAME]"""
    },
    "quote": {
        "default": """Dear [CLIENT NAME],

Thank you for your inquiry. We are pleased to provide you with the following quote:

[INSERT QUOTE DETAILS HERE]

This quote is valid for 30 days. Please confirm if you would like to proceed.

Best regards,
[YOUR NAME]"""
    },
    "complaint": {
        "default": """Dear [CLIENT NAME],

Thank you for bringing this matter to our attention. We sincerely apologize for any inconvenience caused.

We will investigate your complaint thoroughly and take the necessary steps to resolve this matter as quickly as possible. You can expect an update within 24-48 hours.

We appreciate your patience and understanding.

Best regards,
[YOUR NAME]"""
    },
    "information": {
        "default": """Dear Recipient,

Thank you for your inquiry. Here is the information you requested:

[INSERT INFORMATION HERE]

Should you need any further clarification or have additional questions, please feel free to reach out.

Best regards,
[YOUR NAME]"""
    },
    "spam": {
        "default": """We have marked this email as spam. No response will be sent."""
    }
}


def get_template(category: str, template_name: str = "default") -> str:
    """
    Obtenir un template d'email.
    
    Args:
        category: Catégorie de l'email
        template_name: Nom du template (default ou personnalisé)
        
    Returns:
        Contenu du template
    """
    if category in EMAIL_TEMPLATES:
        templates = EMAIL_TEMPLATES[category]
        return templates.get(template_name, templates.get("default", ""))
    return ""


def save_template(category: str, template_name: str, content: str) -> None:
    """
    Sauvegarder un template personnalisé.
    
    Args:
        category: Catégorie
        template_name: Nom du template
        content: Contenu
    """
    if category not in EMAIL_TEMPLATES:
        EMAIL_TEMPLATES[category] = {}
    
    EMAIL_TEMPLATES[category][template_name] = content
    
    # Sauvegarder dans un fichier JSON
    with open("templates/email_templates.json", "w") as f:
        json.dump(EMAIL_TEMPLATES, f, indent=2)


def list_templates(category: str) -> list:
    """Lister les templates d'une catégorie."""
    if category in EMAIL_TEMPLATES:
        return list(EMAIL_TEMPLATES[category].keys())
    return []
