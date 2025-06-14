# 🧠 Exercice 2.2 — Analyse d'Expériences de Prompt Engineering

Ce document présente l’analyse de **trois expériences** de *prompt engineering* réalisées à l’aide d’un modèle de langage (IA) pour générer une fonction en Python.  
Chaque partie décrit le **prompt**, le **code produit**, ainsi qu’une **analyse critique** de la réponse générée.

---

## 🔹 1. Prompt basé sur la Règle *(Zero-Shot Prompting)*

### 📝 Le Prompt
```
Crée une fonction Python format_product_code(product_id). Le product_id doit être une 
chaîne de 10 caractères alphanumériques. La fonction doit insérer un tiret après le 3ème et le 
7ème caractère. Si la chaîne n'a pas 10 caractères ou contient des caractères non 
alphanumériques, elle doit lever une ValueError. Inclue un docstring.
```

### 💻 Réponse IA
```python
def format_product_code1(product_id):
    \"\"\"
    Formate un product_id en insérant des tirets après le 3ème et le 7ème caractère.

    Paramètres:
        product_id (str): Chaîne de 10 caractères alphanumériques.

    Retourne:
        str: Le product_id formaté avec les tirets.

    Soulève:
        ValueError: Si la chaîne n'a pas 10 caractères ou contient des caractères non alphanumériques.
    \"\"\"
    if not isinstance(product_id, str) or len(product_id) != 10 or not product_id.isalnum():
        raise ValueError("Le product_id doit être une chaîne de 10 caractères alphanumériques.")

    return f"{product_id[:3]}-{product_id[3:7]}-{product_id[7:]}"
```

### ✅ Analyse
- **Vérifications d'entrée** : Strictes et appropriées.
- **Gestion d'erreurs** : `ValueError` utilisée de manière adéquate.
- **Formatage** : Lisible avec f-string.
- **Docstring** : Complète et structurée.

---

## 🔹 2. Prompt avec un Exemple *(One-Shot Prompting)*

### 📝 Le Prompt
```
Crée une fonction Python format_product_code(product_id). Le product_id doit être une 
chaîne de 10 caractères alphanumériques. Voici un exemple d'entrée-sortie: 
format_product_code("ABC123DEF4") devrait retourner "ABC-123-DEF4". La fonction doit 
lever une ValueError si l'entrée est invalide. Inclue un docstring.
```

### 💻 Réponse IA
```python
def format_product_code2(product_id):
    \"\"\"
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
    \"\"\"
    if not isinstance(product_id, str) or len(product_id) != 10 or not product_id.isalnum():
        raise ValueError("Le product_id doit être une chaîne de 10 caractères alphanumériques.")

    return f"{product_id[:3]}-{product_id[3:7]}-{product_id[7:]}"
```

### ✅ Analyse comparative

| Critère                  | Version précédente       | Version actuelle             |
|--------------------------|--------------------------|------------------------------|
| Docstring                | Bonne mais sans exemple  | Avec exemple clair           |
| Lisibilité               | Bonne                    | Excellente                   |
| Compréhension            | Nécessite analyse        | Guidée par l’exemple         |
| Prévention d’erreur      | Moyenne                  | Élevée                       |

---

## 🔹 3. Prompt avec Exemples Multiples *(Few-Shot Prompting)*

### 📝 Le Prompt
```
Crée une fonction Python format_product_code(product_id).
Le product_id doit être une chaîne de 10 caractères alphanumériques.
La fonction doit retourner le product_id formaté en insérant un tiret après le 3ᵉ et le 7ᵉ caractère.
La fonction doit lever une ValueError si l'entrée n'est pas une chaîne de 10 caractères alphanumériques.
Inclue un docstring complet avec la description, les paramètres, le retour, les exceptions levées, et deux exemples d'entrée-sortie valides :
format_product_code("ABC123DEF4") devrait retourner "ABC-123-DEF4",
format_product_code("XYZ987GHIJ") devrait retourner "XYZ-987-GHIJ",
ainsi qu’un exemple d’erreur :
format_product_code("SHORT") devrait lever une ValueError.
```

### 💻 Réponse IA
```python
def format_product_code3(product_id):
    \"\"\"
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
    \"\"\"
    if not isinstance(product_id, str) or len(product_id) != 10 or not product_id.isalnum():
        raise ValueError("Le product_id doit être une chaîne de 10 caractères alphanumériques.")

    return f"{product_id[:3]}-{product_id[3:7]}-{product_id[7:]}"
```

### ✅ Analyse critique

#### ✔️ Impact positif des exemples :
- **Moins d’ambiguïté** : Les intentions sont claires.
- **Gestion d’erreurs renforcée** : L’IA comprend mieux les cas invalides.
- **Reproductibilité** : Sorties plus fiables et conformes aux attentes.

#### ⚠️ Limites du Few-Shot Prompting :
- **Nombre excessif d’exemples** :
  - Peut saturer le prompt,
  - Ralentir la génération,
  - Réduire la pertinence.

- **Qualité des exemples** :
  - Des erreurs ou imprécisions peuvent induire l’IA en erreur,
  - Résultats incohérents si les règles sont mal définies.

---

## 📌 Conclusion

Le passage de *zero-shot* à *few-shot* montre une nette amélioration dans la qualité des réponses générées.  
**Les exemples bien choisis et structurés permettent à l’IA de mieux comprendre, généraliser et exécuter les tâches demandées.**

---

> 🧪 Cette analyse met en lumière l’importance de la formulation des prompts pour tirer le meilleur parti des modèles de langage.