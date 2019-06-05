from fixtures.mydb import MyDB

conn = None
cur = None

def setup_module(module):
    global conn, cur
    db = MyDB()
    conn = db.connect("server")
    cur = conn.cursor()

def teardown_module(module):
    cur.close()
    conn.close()

def test_john_id()
    id = cur.execute("select id from employee where name=='john'")
    asset id == 123

def test_tom_id()
    id = cur.execute("select id from employee where name=='tom'")
    asset id == 124
