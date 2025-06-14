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

