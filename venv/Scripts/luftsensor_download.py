# This is a script to download all the csv for one sensor
import datetime
import requests
import sqlite3
import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)

class LuftsensorDownload:

    def download_data(self, year, sensor_type, data_id):
        """
        Methode zum Herunterladen der Daten des entsprechenden Sensors
        :param year:        Jahr der Messungen des Sensors
        :param sensor_type: Den richtigen Sensortypen angeben
        :param data_id:     id des entsprechenden Sensors
        """
        dates = self.get_dates_of_year(year)

        for date in dates:
            filename = '{date}_{sensor_type}_sensor_{data_id}.csv'.format(date=date,sensor_type=sensor_type,data_id=data_id)
            download_path = 'https://archive.sensor.community/{year}/{date}/'.format(year=str(year),date=date)+filename
            response = requests.head(download_path)
            if response.status_code == 200:
                download = requests.get(download_path)
                print(download_path)
                open('venv/Luftsensor_CSV/'+filename,'wb').write(download.content)
                self.import_to_database(filename)
            else:
                print(download_path+ ':'+ response.status_code)


    def import_to_database(self, filename):
        conn = sqlite3.connect('Luftsensor')
        c = conn.cursor()
        c.execute(''' CREATE TABLE IF NOT EXISTS luftsensor_data (
        sensor_id Integer,
        sensor_type VARCHAR,
        location INTEGER,
        lat FLOAT,
        lon FLOAT,
        timestamp TEXT,
        P1 FLOAT,
        durP1 FLOAT,
        ratioP1 FLOAT,
        P2 FLOAT,
        durP2 FLOAT,
        ratioP2 FLOAT ) ''')

        with open('venv/Luftsensor_CSV/'+filename,'r') as csv_file:
            reader = csv.reader(csv_file,delimiter=';')
            next(reader)                    #überspringen der Header-Zeile
            for row in reader:
                c.execute('INSERT INTO luftsensor_data (sensor_id,sensor_type, location, lat, lon, timestamp, P1, durP1, ratioP1, P2, durP2, ratioP2) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)', row)
        conn.commit()
        conn.close()

    def visualize_luftsensor_data(self,sensor_id):
        conn = conn = sqlite3.connect('Luftsensor')
        c = conn.cursor()
        window = Tk()
        fig = Figure(figsize=(15,10),dpi=100)
        plot1 = fig.add_subplot(111)
        xpoints=[]
        ypoints=[]
        dates = self.get_dates_of_year(2022)
        for date in dates:
            date = date[:-3]
            print(date)
            select = "SELECT timestamp,avg(P1) FROM luftsensor_data WHERE sensor_id = {sensor_id} AND timestamp LIKE '{date}%'".format(sensor_id=sensor_id,date=date)
            c.execute(select)
            row = c.fetchall()
            xpoints.append(date)
            ypoints.append(row[0][1])
        plot1.plot(xpoints,ypoints)
        plot1.set_xlabel("Datum")
        plot1.set_ylabel("P1")
        plot1.set_title("Feinstaubwerte für den Sensor {sensor_id}".format(sensor_id=sensor_id))
        labels = xpoints
        plot1.set_xticks(xpoints,labels,rotation='vertical')       # Drehung der Datumse
        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().pack()
        window.title('Feinstaubsensorwerte')
        window.mainloop()

    def get_dates_of_year(self,year):
        """
        Methode zum erstellen eines arrays, in dem alle Datumse des eingegebenen Jahres stehen
        :param year: das Jahr, für das die Datumse gesucht werden müssen
        :return: array für alle Datumse des eingegebenen Jahres
        """
        dates=[]
        start_date = datetime.date(year,1,1)    #erster Tag des Jahres
        end_date = datetime.date(year,12,31)    #letzter Tag des Jahres

        current_date = start_date
        while current_date <= end_date:
            dates.append(current_date.strftime('%Y-%m-%d'))
            current_date += datetime.timedelta(days=1)
        return dates