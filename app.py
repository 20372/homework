from flask import Flask, render_template
import sqlite3
from sqlite3 import Error

app = Flask(__name__)
DATABASE = "Homework"

def create_connection(db_file):
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)
    return None


@app.route('/home_page.html')
def render_home_page():  # put application's code here
    con = create_connection(DATABASE)
    query = "SELECT * FROM Homework"
    cur = con.cursor()
    cur.execute(query)
    students = cur.fetchall()
    con.close()
    return render_template('home_page.html', homework=students)




if __name__ == '__main__':
    app.run()
