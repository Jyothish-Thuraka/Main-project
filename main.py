import os
import eel
from engine.features import *
from engine.command import *
def start():
    eel.init("web")

    playAssistantSound()
    os.system('start msedge.exe --app="http://localhost:8000/index.html"')

    eel.start('index.html', mode=None, host='localhost', block=True)
eel.init("web")

@eel.expose
def get_websites():
    conn = sqlite3.connect('Main.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM websites')
    websites = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return websites

@eel.expose
def add_website(name, url):
    conn = sqlite3.connect('Main.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO websites (name, url) VALUES (?, ?)', (name, url))
    conn.commit()
    conn.close()
    return True

@eel.expose
def update_website(id, name, url):
    conn = sqlite3.connect('Main.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE websites SET name = ?, url = ? WHERE id = ?', (name, url, id))
    conn.commit()
    conn.close()
    return True

@eel.expose
def delete_website(id):
    conn = sqlite3.connect('Main.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM websites WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return True

@eel.expose
def get_contacts():
    conn = sqlite3.connect('Main.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM contacts')
    contacts = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return contacts

@eel.expose
def add_contact(name, mobile_no, email):
    conn = sqlite3.connect('Main.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO contacts (name, mobile_no, email) VALUES (?, ?, ?)', 
                  (name, mobile_no, email))
    conn.commit()
    conn.close()
    return True

@eel.expose
def update_contact(id, name, mobile_no, email):
    conn = sqlite3.connect('Main.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE contacts SET name = ?, mobile_no = ?, email = ? WHERE id = ?', 
                  (name, mobile_no, email, id))
    conn.commit()
    conn.close()
    return True

@eel.expose
def delete_contact(id):
    conn = sqlite3.connect('Main.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM contacts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return True
