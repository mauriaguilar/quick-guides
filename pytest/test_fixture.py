from fixtures.mydb import MyDB

import pytest

@pytest.fixture()
def cur():
    db = MyDB()
    conn = db.connect("server")
    curs = conn.cursor()
    # return curs # asi se crea uno por test
    yield curs # asi se crea una sola vez
    curs.close() # va con el yield
    conn.close() # va con el yield
    print("teardown")

def test_john_id(cur)
    id = cur.execute("select id from employee where name=='john'")
    asset id == 123

def test_tom_id(cur)
    id = cur.execute("select id from employee where name=='tom'")
    asset id == 124

# Evita el uso de variables globales
# y usa injección de dependencias