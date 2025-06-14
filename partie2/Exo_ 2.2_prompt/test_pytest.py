import pytest

from format_product_code import format_product_code1, format_product_code2, format_product_code3

#  Liste des fonctions à tester
functions_to_test = [format_product_code1, format_product_code2, format_product_code3]

@pytest.mark.parametrize("func", functions_to_test)
def test_format_valid_product_code(func):
    assert func("ABC123DEF4") == "ABC-123-DEF4"
    assert func("XYZ987GHIJ") == "XYZ-987-GHIJ"

@pytest.mark.parametrize("func", functions_to_test)
@pytest.mark.parametrize("invalid_input", [
    "SHORT",                # Trop court
    "TOOLONG123456",        # Trop long
    "ABC123!@#%",           # Caractères non alphanumériques
    1234567890,             # Mauvais type
    None,                   # Valeur nulle
])
def test_format_invalid_product_code(func, invalid_input):
    with pytest.raises(ValueError):
        func(invalid_input)
