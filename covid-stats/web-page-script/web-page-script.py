import mariadb
from flask import Flask
from flask import render_template

app = Flask(__name__)
mydb = mariadb.connect(host="some-mariadb",user="marc",password="mypass", database="covidstats")

@app.route('/')
def hello():
    cursor = mydb.cursor()
    cursor.execute("SELECT record_date, confirmed, active, recovered, deaths FROM dailystats ORDER BY record_date DESC")
    rows = cursor.fetchall()
    return render_template('list-cases.html', rows=rows)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

