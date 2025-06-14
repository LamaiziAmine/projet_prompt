# 🧪 Analyse d'Expériences de Prompt Engineering

Ce document regroupe l’analyse de deux séries d’expériences de prompt engineering, chacune explorant différentes approches pour générer des fonctions Python à l’aide d’un modèle d’intelligence artificielle (IA). Chaque série évalue la qualité du code produit selon le type de prompt utilisé.

---

## ✅ Exercice 2.1 — Fonction `calculate(a, b, op)`

---

### 🟡 Prompt Vague

**🔹 Le Prompt :**
```
"Écris une fonction pour faire des opérations entre deux nombres en Python."
```
**🔹 Réponse AI :**
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
```
### répense de la question
* **Nom de la fonction :** `calculate1`.
* **Opérations prises en charge :** Addition (`+`), soustraction (`-`), multiplication (`*`), division (`/`).
* **Gestion des erreurs :** Oui, pour la division par zéro et les opérateurs invalides. Les erreurs sont retournées sous forme de chaînes de caractères (`str`).
* **Commentaires :** Oui.

---

### 🟡 Prompt  Spécifique :

**🔹 Le Prompt :**
```
"Écris une fonction Python appelée calculate(a, b, op) qui prend deux entiers a et b, et une 
chaîne op indiquant '+', '-', '*', ou '/'. La fonction doit retourner le résultat de l’opération, gérer 
les erreurs (division par zéro, opération invalide) et arrondir le résultat de la division à deux 
décimales. Ajoute un docstring détaillé et des commentaires." 
```
**🔹 Réponse AI :**
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

## 🔵 Prompt avec Persona

**🔹 Le Prompt :**
```
"En tant que développeur Python, écris une fonction calculate(a, b, op) qui prend deux entiers et une chaîne représentant une opération mathématique ('+', '-', '*', '/'). La fonction doit être robuste, bien documentée, gérer les erreurs (division par zéro, opérateur invalide), arrondir les divisions à deux décimales, et respecter les conventions PEP8. Inclue un docstring et des commentaires clairs."
```

**🔹 Réponse AI :**
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
## ✅ Réponse à la question

La dernière version du code est plus **professionnelle**, **structurée** et **sécurisée**, pour plusieurs raisons :

### 🧑‍💻 Professionnalisme
- Respect des conventions **PEP8**, assurant un code propre et lisible.
- Utilisation d’un **dictionnaire** pour simplifier la logique et éviter les répétitions.

### 🧱 Structuration améliorée
- Code **plus compact et clair**, sans nuire à la lisibilité.
- Gestion explicite des erreurs (`ZeroDivisionError`, `ValueError`) avant l'exécution.

### 🔐 Sécurité renforcée
- **Vérification de l’opérateur** avant d’accéder au dictionnaire, prévenant les erreurs inattendues.
- **Exceptions bien définies** pour éviter tout comportement indésirable.

---

## 🧠 Analyse Critique

### 1. 🔍 Différences entre les versions générées

- **Prompt Vague**  
  Code fonctionnel mais **peu rigoureux**. Manque d’annotations, structure faible, et une erreur d’appel de fonction (`calculate` au lieu de `calculate1`).

- **Prompt Spécifique**  
  Meilleure **structuration**, avec annotations de type et gestion des erreurs. L’arrondi est respecté, et l’ensemble est **plus exploitable**.

- **Prompt avec Persona**  
  Version la plus **aboutie** : bien documentée, conforme à **PEP8**, claire, robuste et directement **prête à l’emploi**.

---

### 2. 💡 Principe de Prompt Engineering le plus impactant

> L’introduction d’un **persona** ("développeur Python") a permis de guider l’IA vers un résultat **plus professionnel**, en termes de style, de rigueur et de lisibilité.

---

### 3. ⚠️ Erreurs ou comportements inattendus

- **Prompt Vague** : mauvaise référence de fonction (`calculate` → `calculate1`).
- **Prompt Spécifique** : faute de frappe (`calculat2e` → `calculate2`).
- Les autres prompts n’ont pas d’erreurs majeures, mais une **relecture humaine** reste nécessaire.

---

### 4. ⏱️ Coût en temps et effort selon le prompt

| Type de Prompt       | Coût en effort | Détails                                   |
|----------------------|----------------|-------------------------------------------|
| Prompt Vague         | 🚧 Élevé       | Reprise complète (noms, erreurs, structure). |
| Prompt Spécifique    | ⚒️ Modéré      | Quelques ajustements mineurs.             |
| Prompt avec Persona  | ✅ Minimal      | Résultat quasi prêt à l’usage.            |
