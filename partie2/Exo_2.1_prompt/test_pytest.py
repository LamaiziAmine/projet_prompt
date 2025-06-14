import pytest
from calculate import calculate1, calculate2, calculate3  # Assurez-vous que le fichier contenant les fonctions est nommé calculate.py

@pytest.mark.parametrize("func, a, b, op, expected", [
    (calculate1, 5, 3, '+', 8),
    (calculate1, 5, 3, '-', 2),
    (calculate1, 5, 3, '*', 15),
    (calculate1, 5, 3, '/', 1.67),
    (calculate2, 10, 2, '+', 12),
    (calculate2, 10, 2, '-', 8),
    (calculate2, 10, 2, '*', 20),
    (calculate2, 10, 2, '/', 5.0),
    (calculate3, 7, 2, '+', 9),
    (calculate3, 7, 2, '-', 5),
    (calculate3, 7, 2, '*', 14),
    (calculate3, 7, 2, '/', 3.5)
])
def test_calculate_valid_operations(func, a, b, op, expected):
    """Test des opérations valides pour toutes les versions de la fonction."""
    assert func(a, b, op) == expected

@pytest.mark.parametrize("func", [calculate1, calculate2, calculate3])
def test_calculate_division_by_zero(func):
    """Test de la division par zéro pour toutes les versions."""
    with pytest.raises(ZeroDivisionError):
        func(5, 0, '/')

@pytest.mark.parametrize("func, op", [
    (calculate1, '%'),
    (calculate2, '^'),
    (calculate3, 'sqrt')
])
def test_calculate_invalid_operation(func, op):
    """Test des opérations invalides pour toutes les versions."""
    with pytest.raises(ValueError):
        func(5, 3, op)

if __name__ == "__main__":
    pytest.main()
