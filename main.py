# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from Scripts.luftsensor_download import LuftsensorDownload
from tkinter import *
import argparse

def get_luftsensor_data():#year, sensor_type, sensor_id):
    luftsensor_data = LuftsensorDownload()
    year = txt_year.get()
    sensor_id = txt_id.get()
    if not luftsensor_data.check_database(year, sensor_id):
        download = luftsensor_data.download_data(year, "sds011", sensor_id)
        if not download:
            window =Tk()
            window.title("Fehler")
            label = Label(window,text="Für diese Parameter wurde kein Sensor gefunden.")
            label.grid(column=0,row=0)
            window.mainloop()
        else:
            luftsensor_data.visualize_luftsensor_data(year, sensor_id)
    else:
        luftsensor_data.visualize_luftsensor_data(year, sensor_id)
    print(luftsensor_data.average(year,sensor_id))
    print(luftsensor_data.maximum(year, sensor_id))
    print(luftsensor_data.minimum(year, sensor_id))

if __name__ == '__main__':
    #parser = argparse.ArgumentParser()
    #parser.add_argument('-y',
    #                    '--year',
    #                    required=True,
    #                    help="Gib das Jahr an, für das die Daten des Feinstaubsensors angezeigt werden sollen.")
    #parser.add_argument('-si',
    #                    '--sensor_id',
    #                    required=True,
    #                    help="Gib die Id des entsprechenden Sensors an.")
    #parser.add_argument('-st',
    #                    '--sensor_type',
    #                    required=True,
    #                    help="Gib den Sensor-Typen an.")
    #args = parser.parse_args()
    #get_luftsensor_data(args.year, args.sensor_type, args.sensor_id)
    #get_luftsensor_data(2022,'sds011',3280)

    window = Tk()
    window.title("Feinstaubsensor")
    window.geometry('350x200')
    label_year = Label(window,text="Hier bitte das Jahr eintragen:")
    label_year.grid(column=0,row=1)
    txt_year = Entry(window,width=10)
    txt_year.grid(column=1,row=1)
    label_id = Label(window,text="Hier bitt die Sensor Id eintragen:")
    label_id.grid(column=0,row=2)
    txt_id = Entry(window,width=10)
    txt_id.grid(column=1,row=2)
    btn = Button(window,text="Starte Analyse",command=get_luftsensor_data)
    btn.grid(column=0,row=3)
    window.mainloop()

