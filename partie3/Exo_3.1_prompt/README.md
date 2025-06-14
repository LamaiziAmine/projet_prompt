## 🧩 Exercice 3.1 – Analyse et correction d’une erreur d’exécution Python

---

### ❓ Question 1 – Problème à l’exécution

Lors de l’exécution du code, Python renvoie l’erreur suivante :

TypeError: unsupported operand type(s) for +=: 'int' and 'str'

#### 🎯 Pourquoi cette erreur ?
Parce que la liste contient une **chaîne de caractères** `'three'`. Python ne peut pas effectuer une addition entre un **entier (`int`)** et une **chaîne (`str`)**.

---

### 🕵️‍♂️ Question 2 – Analyse de l’erreur

Le problème provient de cette ligne :
```python
my_nums = [1, 2, 'three', 4]  # <-- Erreur ici
```
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

### 🕵️‍♂️ Question 3

```python
import pytest
from calculate_average import calculate_average  # Assurez-vous d'importer la fonction correcte

def test_average_with_valid_numbers():
    """Test avec une liste valide de nombres."""
    assert calculate_average([1, 2, 3, 4]) == 2.5
    assert calculate_average([10, 20, 30, 40]) == 25.0
    assert calculate_average([5]) == 5.0

def test_average_with_negative_numbers():
    """Test avec des nombres négatifs."""
    assert calculate_average([-1, -2, -3, -4]) == -2.5
    assert calculate_average([-10, -20, -30]) == -20.0

def test_average_with_mixed_numbers():
    """Test avec un mélange de nombres positifs et négatifs."""
    assert calculate_average([-5, 0, 5, 10]) == 2.5

def test_average_with_invalid_values():
    """Test avec une liste contenant des valeurs non numériques."""
    with pytest.raises(ValueError):
        calculate_average([1, 2, 'three', 4])  # Contient une chaîne de caractères

    with pytest.raises(ValueError):
        calculate_average([1, 2, None, 4])  # Contient `None`

    with pytest.raises(ValueError):
        calculate_average(['a', 'b', 'c'])  # Liste contenant uniquement des chaînes

def test_average_with_empty_list():
    """Test avec une liste vide (devrait lever une erreur)."""
    with pytest.raises(ZeroDivisionError):
        calculate_average([])
```

 