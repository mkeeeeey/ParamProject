import sqlite3


# COMBO BOX ITEM OF SELECT MODEL
def modelBox():
    conn, cur = None, None
    conn = sqlite3.connect("./nex.db")
    cur = conn.cursor()

    cur.execute("SELECT model_name FROM MODEL WHERE model_id in (11,12,13,14)")
    model = []
    for item in cur.fetchall():
        model.append(item[0])
    conn.close()

    return model


# CURRENT LANGUAGE
def getLang():
    conn, cur = None, None
    conn = sqlite3.connect("./nex.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM LOCALE;")
    lang = cur.fetchone()[0]
    conn.close()

    return lang


# CHANGE LANGUAGE
def setLang(lang):
    conn, cur = None, None
    conn = sqlite3.connect("./nex.db")
    cur = conn.cursor()

    if lang == 'kor':
        query = cur.execute("UPDATE LOCALE SET language = 'kor'")
    else:
        query = cur.execute("UPDATE LOCALE SET language = 'eng'")

    conn.commit()
    conn.close()


# INDEX LIST OF EACH MODE
def listIdx(mode):
    conn, cur = None, None
    conn = sqlite3.connect("./nex.db")
    cur = conn.cursor()

    list = []
    cur.execute('SELECT cate_id FROM CATEGORY WHERE mode_id = ?;',(mode,))
    for idx in cur.fetchall():
        list.append(idx[0])
    conn.close()

    return list


# SP COMBOBOX ITEM
def itemBox(lang, group):
    conn, cur = None, None
    conn = sqlite3.connect("./nex.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM ITEM WHERE item_group = ?", (group,))
    model = []
    for item in cur.fetchall():
        if lang == 'kor':
            model.append(item[1])
        else:
            model.append(item[2])
    conn.close()
    print(model)

    return model


# MIN/MAX VALUE ON SENSOR TYPE
def getVal(id):
    conn, cur = None, None
    conn = sqlite3.connect("./nex.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM VALUE WHERE item_id = ?", (id,))
    data = cur.fetchall()
    conn.close()
    print(data)

    return data


# COMBOBOX OF SENSOR
def typeBox(group):
    conn, cur = None, None
    conn = sqlite3.connect("./nex.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM ITEM WHERE item_group = ?", (group,))
    data = cur.fetchall()
    conn.close()

    return data