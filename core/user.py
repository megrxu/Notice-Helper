import sqlite3


def get_conn():
    conn = sqlite3.connect('data/data.db')
    db = conn.cursor()
    return (conn, db)


def if_new_user(chat_id):
    conn, db = get_conn()
    db.execute('SELECT * FROM users WHERE id=?', (chat_id,))
    result = db.fetchall()
    conn.close()
    if result:
        return False
    else:
        return True


def get_users():
    conn, db = get_conn()
    db.execute('SELECT * FROM users')
    result = db.fetchall()
    conn.close()
    return result


def add_user(chat_id, subs):
    conn, db = get_conn()
    db.execute('INSERT INTO users VALUES (?,?)', (chat_id, subs))
    conn.commit()
    conn.close()


def get_subs(chat_id):
    conn, db = get_conn()
    db.execute('SELECT subs FROM users WHERE id=?', (chat_id,))
    subs = db.fetchall()
    conn.close()
    return subs[0][0].split(';')


def add_subs(chat_id, sub):
    subs = get_subs(chat_id)
    subs.append(sub)
    subs = ';'.join(subs)
    update_subs(chat_id, subs)


def del_subs(chat_id, sub):
    subs = get_subs(chat_id)
    subs.remove(sub)
    subs = ';'.join(subs)
    update_subs(chat_id, subs)


def update_subs(chat_id, subs):
    conn, db = get_conn()
    db.execute('UPDATE users SET subs=? WHERE id=?', (subs, chat_id))
    conn.commit()
    conn.close()
