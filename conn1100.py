import sqlite3


# INITIALIZE VARIABLE
def setVar():
    conn, cur = None, None
    conn = sqlite3.connect("./nex.db")
    cur = conn.cursor()

    cur.execute('SELECT * FROM NEX1100;')
    data = cur.fetchall()
    conn.close()

    return data


# USER MODE TREE
def userTree():
    conn, cur = None, None
    sql = '''WITH RECURSIVE parent(cate_id, cate_level, cate_name, cate_eng, LEVEL) AS 
    ( 
        SELECT cate_id, cate_level, cate_name, cate_eng, 0 level FROM CATEGORY 
        WHERE cate_level IS NULL AND mode_id = 1 AND model_id IN (10, 11, 12)
        UNION ALL 
        SELECT c.cate_id, c.cate_level, c.cate_name, c.cate_eng, parent.LEVEL+1 
        FROM CATEGORY c
        JOIN parent ON c.cate_level=parent.cate_id 
        ORDER BY 2 DESC, cate_id
    ) 
    SELECT * FROM parent;'''

    conn = sqlite3.connect("./nex.db")
    cur = conn.cursor()

    cur.execute(sql)
    data = cur.fetchall()
    conn.close()

    return data


# ADMIN MODE TREE
def adminTree():
    conn, cur = None, None
    sql = '''WITH RECURSIVE parent(cate_id, cate_level, cate_name, cate_eng, LEVEL) AS 
    ( 
        SELECT cate_id, cate_level, cate_name, cate_eng, 0 level FROM CATEGORY 
        WHERE cate_level IS NULL AND mode_id = 2 AND model_id IN (10, 11, 12)
        UNION ALL 
        SELECT c.cate_id, c.cate_level, c.cate_name, c.cate_eng, parent.LEVEL+1 
        FROM CATEGORY c
        JOIN parent ON c.cate_level=parent.cate_id 
        ORDER BY 2 DESC, cate_id 
    ) 
    SELECT * FROM parent;'''

    conn = sqlite3.connect("./nex.db")
    cur = conn.cursor()

    cur.execute(sql)
    data = cur.fetchall()
    conn.close()

    return data


# TITLE OF TABLE PAGE
def getTitle(index):
    conn, cur = None, None
    conn = sqlite3.connect("./nex.db")
    cur = conn.cursor()

    parent = (109, 112, 123, 124, 144, 145, 146, 167, 155, 156, 157, 152, 180, 181, 183)

    sql1 = '''SELECT cate_name, cate_eng FROM CATEGORY
    WHERE cate_id  = (SELECT c.cate_level FROM CATEGORY c WHERE c.cate_id = ?)'''

    sql2 = '''SELECT cate_name, cate_eng FROM CATEGORY WHERE cate_id = ?'''

    if index in parent:
        cur.execute(sql2, (index,))
    else:
        cur.execute(sql1, (index,))
    data = cur.fetchall()[0]
    conn.close()

    return data


# TABLE ITEM
def getTable(index):
    conn, cur = None, None
    conn = sqlite3.connect("./nex.db")
    cur = conn.cursor()

    cur.execute('SELECT * FROM NEX1100 WHERE cate_id = ?', (index,))
    data = cur.fetchall()
    conn.close()

    return data


# GET KEY1 KEY2 FOR CHANGE EU AND EUS
# KEY1 = mainID KEY2 = tagID
def eu1(ch):
    conn, cur = None, None
    conn = sqlite3.connect("./nex.db")
    cur = conn.cursor()

    if ch == 1:
        cur.execute('''SELECT n.param_id, n.param_min, n.param_max FROM NEX1100 n
        WHERE n.param_min = '-200.0' AND n.param_max = '1370.0'
        AND n.cate_id IN (SELECT c.cate_id FROM CATEGORY c WHERE c.cate_eng = 'CH1' AND c.model_id = 12);''')
    elif ch == 2:
        cur.execute('''SELECT n.param_id, n.param_min, n.param_max FROM NEX1100 n
        WHERE n.param_min = '-200.0' AND n.param_max = '1370.0'
        AND n.cate_id IN (SELECT c.cate_id FROM CATEGORY c WHERE c.cate_eng = 'CH2' AND c.model_id = 12);''')
    else:
        cur.execute('''SELECT n.param_id, n.param_min, n.param_max FROM NEX1100 n
        WHERE n.param_min = '-200.0' AND n.param_max = '1370.0'
        AND n.cate_id IN (SELECT c.cate_id FROM CATEGORY c WHERE c.model_id = 12);''')

    data = cur.fetchall()
    conn.close()

    return data


def eus1(ch):
    conn, cur = None, None
    conn = sqlite3.connect("./nex.db")
    cur = conn.cursor()

    if ch == 1:
        cur.execute('''SELECT n.param_id, n.param_min, n.param_max FROM NEX1100 n
        WHERE n.param_min = '0.0' AND n.param_max = '1570.0'
        AND n.cate_id IN (SELECT c.cate_id FROM CATEGORY c WHERE c.cate_eng = 'CH1' AND c.model_id = 12);''')
    elif ch == 2:
        cur.execute('''SELECT n.param_id, n.param_min, n.param_max FROM NEX1100 n
        WHERE n.param_min = '0.0' AND n.param_max = '1570.0'
        AND n.cate_id IN (SELECT c.cate_id FROM CATEGORY c WHERE c.cate_eng = 'CH2' AND c.model_id = 12);''')
    else:
        cur.execute('''SELECT n.param_id, n.param_min, n.param_max FROM NEX1100 n
        WHERE n.param_min = '0.0' AND n.param_max = '1570.0'
        AND n.cate_id IN (SELECT c.cate_id FROM CATEGORY c WHERE c.model_id = 12);''')

    data = cur.fetchall()
    conn.close()

    return data
