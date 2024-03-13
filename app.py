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


@app.route('/')
def render_menu():
   return render_template('home_page.html')

@app.route('/home_page.html')
def render_home_page():  # put application's code here
    con = create_connection(DATABASE)
    query = "SELECT First_Name, Last_Name, title, job_type FROM Homework INNER JOIN Students1_dg_tmp ON Students1_dg_tmp.Id = Homework.student_id INNER JOIN Work ON Work.Id = work_id"
    cur = con.cursor()
    cur.execute(query)
    students = cur.fetchall()
    con.close()
    return render_template('home_page.html', homework=students)




if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
