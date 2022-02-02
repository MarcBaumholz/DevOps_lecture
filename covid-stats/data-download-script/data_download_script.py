import datefinder as datefinder
import requests
import time
import mariadb

endpoint_url = 'https://api.covid19api.com/country/malta'
response = requests.get(endpoint_url)
json_response = response.json()


while True:
    print("Executing")

    mydb = mariadb.connect(host="some-mariadb",user="marc",password="mypass", database="covidstats")
    
    cursor = mydb.cursor()
    cursor.execute("delete from dailystats")

    for day in json_response:
        confirmed = day['Confirmed']
        deaths = day['Deaths']
        active = day['Active']
        recovered = day['Recovered']

        matches = datefinder.find_dates(day['Date'])
        date = None

        for match in matches:
            date = match
            break
        cursor.execute("""
        INSERT INTO dailystats(record_date, confirmed, active, recovered, deaths) values (?,?,?,?,?)
        """, (date, confirmed, active, recovered, deaths))
        mydb.commit()

    mydb.close()
    time.sleep(120)


