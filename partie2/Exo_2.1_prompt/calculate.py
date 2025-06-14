def calculate1(a, b, operation):
    """
    Effectue une opération mathématique entre deux nombres.

    Args:
        a (float): Premier nombre.
        b (float): Deuxième nombre.
        operation (str): Opération à effectuer ('+', '-', '*', '/').

    Returns:
        float: Résultat de l'opération.

    Raises:
        ValueError: Si l'opération n'est pas valide.
        ZeroDivisionError: Si une division par zéro est tentée.
    """
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b == 0:
            raise ZeroDivisionError("Division par zéro non autorisée.")
        return round(a / b, 2)
    else:
        raise ValueError("Opération non valide. Utilisez '+', '-', '*' ou '/'.")

# Exemple d'utilisation
print(calculate1(5, 3, '+'))  # 8
print(calculate1(5, 3, '-'))  # 2
print(calculate1(5, 3, '*'))  # 15
print(calculate1(5, 3, '/'))  # 1.67

def calculate2(a: int, b: int, op: str) -> float:
    """
    Effectue une opération mathématique entre deux entiers.

    Args:
        a (int): Premier nombre entier.
        b (int): Deuxième nombre entier.
        op (str): Opération à effectuer ('+', '-', '*', '/').

    Returns:
        float: Résultat de l'opération.

    Raises:
        ValueError: Si l'opération n'est pas valide.
        ZeroDivisionError: Si une division par zéro est tentée.
    """
    
    # Vérification de l'opération demandée
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            raise ZeroDivisionError("Division par zéro non autorisée.")
        return round(a / b, 2)
    else:
        raise ValueError("Opération non valide. Utilisez '+', '-', '*' ou '/'.")

# Exemple d'utilisation
if __name__ == "__main__":
    try:
        print(calculate2(5, 3, '+'))  # 8
        print(calculate2(5, 3, '-'))  # 2
        print(calculate2(5, 3, '*'))  # 15
        print(calculate2(5, 3, '/'))  # 1.67
        print(calculate2(5, 0, '/'))  # Lève une ZeroDivisionError
    except Exception as e:
        print(f"Erreur: {e}")

def calculate3(a: int, b: int, op: str) -> float:
    """
    Effectue une opération mathématique entre deux entiers.

    Args:
        a (int): Premier nombre entier.
        b (int): Deuxième nombre entier.
        op (str): Opérateur mathématique ('+', '-', '*', '/').

    Returns:
        float: Résultat de l'opération arrondi à deux décimales.

    Raises:
        ValueError: Si l'opération n'est pas valide.
        ZeroDivisionError: Si une division par zéro est tentée.
    """
    # Vérification de l'opérateur et exécution de l'opération
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            raise ZeroDivisionError("Division par zéro non autorisée.")
        return round(a / b, 2)
    else:
        raise ValueError("Opération non valide. Utilisez '+', '-', '*' ou '/'.")


# Exemple d'utilisation
if __name__ == "__main__":
    try:
        print(calculate3(10, 2, '+'))  # 12
        print(calculate3(10, 2, '-'))  # 8
        print(calculate3(10, 2, '*'))  # 20
        print(calculate3(10, 2, '/'))  # 5.0
        print(calculate3(10, 0, '/'))  # Lève une ZeroDivisionError
    except Exception as e:
        print(f"Erreur: {e}")

