import code

def test_sum():
    assert(code.sum(1,2), 3)

def test_mul():
    assert(code.mul(1,2), 2)

# Correr tests:
#   python -m pytest -v
#   -v: mostrar PASSED
#   py.test
# pytest -v
# pytest -v --capture=no # no captura los prints
# pytest --capture=no # muestra con puntos la cantidad de test