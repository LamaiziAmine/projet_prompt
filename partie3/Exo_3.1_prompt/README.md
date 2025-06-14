------------------------------------------
|               exercice 3.1             |
------------------------------------------

## Question 1
**Problème à l’exécution :**
Lorsque tu exécutes ce code, Python lève une erreur :

TypeError: unsupported operand type(s) for +=: 'int' and 'str'
**Pourquoi cette erreur ?**
Parce que la liste contient une chaîne de caractères 'three', et Python ne peut pas additionner un entier (int) avec une chaîne (str)

## Question 2 
**Analyse de l'erreur**
Le problème dans ton code vient de la ligne suivante :

**my_nums = [1, 2, 'three', 4] # <-- Error here**

Tu inclues une chaîne de caractères ('three') dans une liste censée contenir uniquement des nombres (int ou float). Lors de la boucle for num in numbers_list:, Python tente d'ajouter 'three' à total, ce qui entraîne une TypeError, car on ne peut pas additionner un entier avec une chaîne.

## la correction proposée
```python
def calculate_average(numbers_list):
    """
    Calcule la moyenne des nombres présents dans une liste.

    Paramètres:
        numbers_list (list): Liste contenant uniquement des nombres (int ou float).

    Retourne:
        float: La moyenne des nombres de la liste.

    Soulève:
        ValueError: Si la liste contient des éléments non numériques.
    """
    if not all(isinstance(num, (int, float)) for num in numbers_list):
        raise ValueError("La liste ne doit contenir que des nombres (int ou float).")

    return sum(numbers_list) / len(numbers_list)

# Exemple d'utilisation
try:
    my_nums = [1, 2, 'three', 4]  # Erreur détectée ici
    avg = calculate_average(my_nums)
    print(f"Moyenne: {avg}")
except ValueError as e:
    print(f"Erreur: {e}")

# Test valide
print(calculate_average([1, 2, 3, 4]))  # Sortie: 2.5
```

## Question 3
 