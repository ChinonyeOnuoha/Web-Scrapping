from bs4 import BeautifulSoup
import  requests
import pymysql.cursors
import csv


        
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='Covid_data',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)



def create_table():
    # Creating a cursor object using the cursor() method
    cursor = connection.cursor()
    # Drop the existing pandemic record
    cursor.execute('DROP TABLE IF EXISTS pandemic')
    # Create a new pandemic table
    sql = "CREATE TABLE pandemic(id INT(11) AUTO_INCREMENT NOT NULL PRIMARY KEY, Country VARCHAR(100), Cases CHAR(255) , Deaths CHAR(255), Recoveries CHAR(255))"
    # Run created table
    cursor.execute(sql)
 # Call the table function          
create_table()


def open_csv():
    # Creating a cursor object using the cursor() method
    cursor = connection.cursor()
    #Open csv file
    with open('covid_data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        # Loop through the csv file
        for row in csv_reader:
            # print(row)
            Country = row[0]
            Cases = row[1]
            Deaths = row[2]
            Recoveries = row[3]
            pandemic_data = f"INSERT INTO pandemic(Country, Cases, Deaths, Recoveries) VALUES('{Country}', '{Cases}', '{Deaths}', '{Recoveries}')"
            cursor.execute(pandemic_data)
            connection.commit()
    # Close connenction to database
    connection.close()   

open_csv()        


def write_to_csv(data):

    file = open('covid_data.csv', 'a')
    file.write(f'{data[0]},{data[1]},{data[2]},{data[3]}\n')
    file.close()


data = requests.get('https://en.wikipedia.org/wiki/COVID-19_pandemic_by_country_and_territory')

wiki_soup = BeautifulSoup(data.content, features='html.parser')

world_data = wiki_soup.find('tr', {'class':'sorttop'})
world_data_cells = world_data.find_all('th')

world_cases, world_deaths, world_recoveries = world_data_cells[2].get_text(), world_data_cells[3].get_text(), world_data_cells[4].get_text()

world_cases = world_cases.replace(',', '').replace('\n', '')
world_deaths = world_deaths.replace(',', '').replace('\n', '')
world_recoveries = world_recoveries.replace(',', '').replace('\n', '')

write_to_csv(['Global',world_cases,world_deaths,world_recoveries])


other_countries = wiki_soup.find('div', {'id':'covid19-container'}).find_all('tr')

for row in other_countries:
    row_cells = row.find_all('td')

    try:

        country_name = row.find('a').get_text()
        # print(country_name.get_text())

        row_cells_cases, row_cells_deaths, row_cells_recoveries = row_cells[0].get_text(), row_cells[1].get_text(), row_cells[2].get_text()
        # print(row_cells_cases, row_cells_deaths, row_cells_recoveries)

        country_name = country_name.replace(',', '').replace('\n', '')
        row_cells_cases = row_cells_cases.replace(',', '').replace('\n', '')
        row_cells_deaths = row_cells_deaths.replace(',', '').replace('\n', '')
        row_cells_recoveries = row_cells_recoveries.replace(',', '').replace('\n', '')


        write_to_csv([country_name, row_cells_cases, row_cells_deaths, row_cells_recoveries])

    except:
        pass


     

# print(world_data.get_text())
