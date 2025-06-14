------------------------------------------------------------
|                       exercice 2.2                        |
------------------------------------------------------------


# Analyse d'Expériences de Prompt Engineering

Ce document présente l’analyse de trois expériences de prompt engineering réalisées à l’aide d’un modèle de langage (IA) pour générer une fonction en Python. Chaque partie décrit le prompt employé, le code produit, ainsi qu’une analyse critique de la réponse générée.

---

## Prompt basé sur la Règle (zéro-Shot Prompting) : 

### Le Prompt
```
"Crée une fonction Python format_product_code(product_id). Le product_id doit être une 
chaîne de 10 caractères alphanumériques. La fonction doit insérer un tiret après le 3ème et le 
7ème caractère. Si la chaîne n'a pas 10 caractères ou contient des caractères non 
alphanumériques, elle doit lever une ValueError. Inclue un docstring."  
```
### répense AI
```python
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
```
### répense de la question
Oui, le code est correct et robuste. Voici une évaluation détaillée :

1. Vérification stricte des entrées :
isinstance(product_id, str) : s'assure que l'entrée est bien une chaîne.
len(product_id) != 10 : garantit que la longueur est exactement 10.
product_id.isalnum() : empêche tout caractère non alphanumérique.

2. Levée explicite d’erreur :
L’exception ValueError est bien choisie, ce qui permet de gérer proprement les cas invalides.

3. Formatage clair :
Utilisation du f-string pour une lecture fluide : "{product_id[:3]}-{product_id[3:7]}-{product_id[7:]}".

4. Docstring bien structurée :
Explication du but de la fonction, des paramètres, du retour, et des exceptions — parfait pour la documentation ou les outils comme Sphinx.

## Prompt avec un Exemple (One-Shot Prompting) :

### Le Prompt
```
"Crée une fonction Python format_product_code(product_id). Le product_id doit être une 
chaîne de 10 caractères alphanumériques. Voici un exemple d'entrée-sortie: 
format_product_code("ABC123DEF4") devrait retourner "ABC-123-DEF4". La fonction doit 
lever une ValueError si l'entrée est invalide. Inclue un docstring." 
```

### répense AI
```python 
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
```
### répense de la question

**Version précédente:**
1. Docstring:	Description correcte mais sans exemple d'appel
2. Lisibilité:	Bonne
3. Compréhension:  IA	Nécessite d’analyser le code pour en déduire l’effet
4. Prévention d'erreur: 	Moyenne : dépend de la capacité à interpréter

**Version actuelle**
1. Docstring:	Description + exemple concret (>>>)
2. Lisibilité:	Excellente : l’exemple montre directement l'usage
3. Compréhension:  L’exemple guide l’interprétation automatiquement
4. Prévention d'erreur: 	Élevée : montre ce qui est attendu exactement

## Prompt avec Multiple Exemples (Few-Shot prompting) :  

### Le Prompt
```
"Crée une fonction Python format_product_code(product_id).
Le product_id doit être une chaîne de 10 caractères alphanumériques.
La fonction doit retourner le product_id formaté en insérant un tiret après le 3ᵉ et le 7ᵉ caractère.
La fonction doit lever une ValueError si l'entrée n'est pas une chaîne de 10 caractères alphanumériques.
Inclue un docstring complet avec la description, les paramètres, le retour, les exceptions levées, et deux exemples d'entrée-sortie valides :
format_product_code("ABC123DEF4") devrait retourner "ABC-123-DEF4",
format_product_code("XYZ987GHIJ") devrait retourner "XYZ-987-GHIJ",
ainsi qu’un exemple d’erreur :
format_product_code("SHORT") devrait lever une ValueError." 
```

### répense AI
```python 
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
```

### répense de la question
Oui, avec cette version enrichie de ta fonction, l’IA  gère mieux les cas d’erreur, et la robustesse du code est effectivement améliorée.


### Analyse Critique 

1. L’ajout d’exemples explicites améliore considérablement la capacité de l’IA à comprendre et à générer du code correct.
**Impact observé :**
Réduction de l’ambiguïté : L’IA n’a pas besoin d’interpréter les intentions — elle les voit dans les exemples.

Meilleure gestion des erreurs : Si un cas d’erreur est fourni (SHORT ➝ ValueError), l’IA va apprendre qu’un comportement d’exception est attendu.

Réplication exacte du comportement souhaité : Les exemples donnent une cible claire pour la sortie.

2. Le few-shot prompting est utile pour transmettre des formats, des comportements ou des styles que l’IA ne peut pas deviner à partir d’instructions générales.

3. 
**Limites de nombre :**
Trop d’exemples (> 3–5) peuvent :

- Saturer le prompt (surtout si le contexte est limité),
- Diluer l’attention de l’IA,
- Allonger le temps de génération,
- Rendre le modèle moins réactif aux instructions générales.

**Limites de qualité :**
Des exemples incorrects, imprécis ou contradictoires vont :

- Induire l’IA en erreur,
- Produire des sorties incohérentes ou fausses,
- Contaminer la compréhension du format ou des règles.