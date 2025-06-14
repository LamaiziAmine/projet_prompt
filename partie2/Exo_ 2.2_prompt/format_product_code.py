def format_product_code1(product_id):
    """
    Formate un product_id en insérant des tirets après le 3ème et le 7ème caractère.

    Paramètres:
        product_id (str): Chaîne de 10 caractères alphanumériques.

    Retourne:
        str: Le product_id formaté avec les tirets.

    Soulève:
        ValueError: Si la chaîne n'a pas 10 caractères ou contient des caractères non alphanumériques.
    """
    if not isinstance(product_id, str) or len(product_id) != 10 or not product_id.isalnum():
        raise ValueError("Le product_id doit être une chaîne de 10 caractères alphanumériques.")

    return f"{product_id[:3]}-{product_id[3:7]}-{product_id[7:]}"

# Exemple d'utilisation
print(format_product_code1("ABC123DEF4"))  # Sortie: "ABC-123-DEF4"
print(format_product_code1("XYZ987GHIJ"))  # Sortie: "XYZ-987-GHIJ"


def format_product_code2(product_id):
    """
    Formate un product_id en insérant des tirets après le 3ème et le 7ème caractère.

    Paramètres:
        product_id (str): Une chaîne alphanumérique de 10 caractères.

    Retourne:
        str: Le product_id formaté avec des tirets.

    Soulève:
        ValueError: Si la chaîne n'a pas exactement 10 caractères ou contient des caractères non alphanumériques.

    Exemple:
        >>> format_product_code("ABC123DEF4")
        'ABC-123-DEF4'
    """
    if not isinstance(product_id, str) or len(product_id) != 10 or not product_id.isalnum():
        raise ValueError("Le product_id doit être une chaîne de 10 caractères alphanumériques.")

    return f"{product_id[:3]}-{product_id[3:7]}-{product_id[7:]}"

# Exemple d'utilisation
print(format_product_code2("ABC123DEF4"))  # Sortie: "ABC-123-DEF4"
print(format_product_code2("XYZ987GHIJ"))  # Sortie: "XYZ-987-GHIJ"

def format_product_code3(product_id):
    """
    Formate un product_id en insérant des tirets après le 3ᵉ et le 7ᵉ caractère.

    Paramètres:
        product_id (str): Une chaîne de 10 caractères alphanumériques.

    Retourne:
        str: Le product_id formaté avec des tirets.

    Soulève:
        ValueError: Si l'entrée n'est pas une chaîne de 10 caractères alphanumériques.

    Exemples:
        >>> format_product_code("ABC123DEF4")
        'ABC-123-DEF4'

        >>> format_product_code("XYZ987GHIJ")
        'XYZ-987-GHIJ'

        >>> format_product_code("SHORT")
        Traceback (most recent call last):
        ...
        ValueError: Le product_id doit être une chaîne de 10 caractères alphanumériques.
    """
    if not isinstance(product_id, str) or len(product_id) != 10 or not product_id.isalnum():
        raise ValueError("Le product_id doit être une chaîne de 10 caractères alphanumériques.")

    return f"{product_id[:3]}-{product_id[3:7]}-{product_id[7:]}"

# Exemple d'utilisation
print(format_product_code3("ABC123DEF4"))  # Sortie: "ABC-123-DEF4"
print(format_product_code3("XYZ987GHIJ"))  # Sortie: "XYZ-987-GHIJ"