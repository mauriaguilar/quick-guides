import code
import pytest
import sys

@pytest.mark.skip(reason="reason to skip")
def test_sum():
    assert(code.sum(1,2), 3)

print "VERSION: .",sys.version_info,"."
@pytest.mark.skipif(sys.version_info.major > 2,reason="reason to skip")
def test_mul():
    assert(code.mul(1,2), 2)

# Ejecucion:
# python -m pytest -v --capture=no test_skip.py

# Resultado:
# collected 2 items                                                                                                                      
# test_skip.py::test_sum SKIPPED
# test_skip.py::test_mul PASSED


# Ejecutar tests:
# python -m pytest -v --capture=no test_skip.py -k test_


@pytest.mark.windows
def test_mul2_windows():
    assert(code.mul(1,2), 2)

@pytest.mark.mac
def test_mul2_mac():
    assert(code.mul(1,2), 2)

@pytest.mark.linux
def test_mul_linux():
    assert(code.mul(1,2), 2)

# pytest -m windows -v
# pytest -m mac -v
