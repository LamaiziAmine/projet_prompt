------------------------------------------------------------
|                       exercice 2.1                         |
------------------------------------------------------------


# Analyse d'Expériences de Prompt Engineering

Ce document présente l’analyse de trois expériences de prompt engineering réalisées à l’aide d’un modèle de langage (IA) pour générer une fonction en Python. Chaque partie décrit le prompt employé, le code produit, ainsi qu’une analyse critique de la réponse générée.

---

## Prompt Vague :

### Le Prompt
```
"Écris une fonction pour faire des opérations entre deux nombres en Python."
```
### répense AI
```python
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
print(calculate(5, 3, '+'))  # 8
print(calculate(5, 3, '-'))  # 2
print(calculate(5, 3, '*'))  # 15
print(calculate(5, 3, '/'))  # 1.67
```
### répense de la question
* **Nom de la fonction :** `calculate1`.
* **Opérations prises en charge :** Addition (`+`), soustraction (`-`), multiplication (`*`), division (`/`).
* **Gestion des erreurs :** Oui, pour la division par zéro et les opérateurs invalides. Les erreurs sont retournées sous forme de chaînes de caractères (`str`).
* **Commentaires :** Oui.

---

## Prompt  Spécifique :

### Le Prompt
```
"Écris une fonction Python appelée calculate(a, b, op) qui prend deux entiers a et b, et une 
chaîne op indiquant '+', '-', '*', ou '/'. La fonction doit retourner le résultat de l’opération, gérer 
les erreurs (division par zéro, opération invalide) et arrondir le résultat de la division à deux 
décimales. Ajoute un docstring détaillé et des commentaires." 
```
### répense AI
```python

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
        print(calculat2e(5, 0, '/'))  # Lève une ZeroDivisionError
    except Exception as e:
        print(f"Erreur: {e}")
```
### répense de la question
* **Comparaison :** Par rapport à la V1, cette fonction est plus **robuste** car elle gère le cas spécifique de l'arrondi. Sa **lisibilité** est équivalente et sa **couverture des cas** est meilleure grâce à l'ajout de cette fonctionnalité précise.

---

## Prompt Avec Persona

### Le Prompt
```
"En tant que développeur Python, écris une fonction calculate(a, b, op) qui prend deux entiers et une chaîne représentant une opération mathématique ('+', '-', '*', '/'). La fonction doit être robuste, bien documentée, gérer les erreurs (division par zéro, opérateur invalide), arrondir les divisions à deux décimales, et respecter les conventions PEP8. Inclue un docstring et des commentaires clairs."
```

### répense AI
```python 
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
```
### répense de la question
Oui, cette version du code est plus professionnelle, mieux structurée et plus sécurisée pour plusieurs raisons :

* **Professionnalisme**:
Respect des conventions PEP8, garantissant un code propre et lisible.
Utilisation d’un dictionnaire pour simplifier la logique et éviter les répétitions inutiles.

* **Structuration améliorée**:
Le code est plus compact et clair, sans compromettre la lisibilité.
Vérification explicite des erreurs (ZeroDivisionError, ValueError) avant l'exécution de l'opération.

* **Sécurité renforcée**:
Vérification de l’opérateur avant l’accès au dictionnaire, empêchant toute erreur imprévue.
Gestion stricte des erreurs avec des exceptions bien définies pour éviter des comportements indésirables.


### Analyse Critique 

1. Différences observées entre les codes générés
Prompt Vague :
Le code est basique, fonctionnel mais peu rigoureux. Il manque d’annotations de type, d'une structure professionnelle, et contient une erreur d’appel de fonction (calculate au lieu de calculate1).

Prompt Spécifique :
Meilleure structuration avec annotations de type, gestion correcte des erreurs, et respect de la consigne d’arrondi. L’ensemble est plus précis et exploitable.

Prompt avec Persona :
Code le plus abouti, respectant les standards professionnels (PEP8), bien documenté, clair, robuste et prêt à l’emploi.

2. Principe de Prompt Engineering le plus impactant
L’utilisation d’un persona a eu le plus grand impact. En donnant un rôle clair à l’IA ("développeur Python"), le prompt oriente la génération vers un code plus professionnel, structuré et conforme aux bonnes pratiques.

3. Erreurs ou comportements inattendus de l’IA
Dans la version vague, l’IA a mal nommé la fonction dans l’exemple d’appel (calculate au lieu de calculate1).

Dans la version spécifique, une faute de frappe est présente (calculat2e au lieu de calculate2).

Les autres versions ne présentent pas d’erreurs critiques, mais confirment la nécessité de relecture humaine.

4. Coût en temps et en effort selon le type de prompt
Prompt Vague : Coût élevé. Il faut retravailler le code (noms, erreurs, documentation, style).

Prompt Spécifique : Coût modéré. Le code est déjà structuré, peu de modifications nécessaires.

Prompt avec Persona : Coût minimal. Résultat final presque prêt à l’emploi.

