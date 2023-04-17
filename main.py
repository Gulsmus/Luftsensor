# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from Scripts.luftsensor_download import LuftsensorDownload
import argparse

def get_luftsensor_data(year, sensor_type, sensor_id):
    luftsensor_data = LuftsensorDownload()
    if luftsensor_data.check_database(year, sensor_id):
        luftsensor_data.visualize_luftsensor_data(year, sensor_id)
    else:
        luftsensor_data.download_data(year, sensor_type, sensor_id)
        luftsensor_data.visualize_luftsensor_data(year, sensor_id)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-y',
                        '--year',
                        required=True,
                        help="Gib das Jahr an, für das die Daten des Feinstaubsensors angezeigt werden sollen.")
    parser.add_argument('-si',
                        '--sensor_id',
                        required=True,
                        help="Gib die Id des entsprechenden Sensors an.")
    parser.add_argument('-st',
                        '--sensor_type',
                        required=True,
                        help="Gib den Sensor-Typen an.")
    args = parser.parse_args()
    get_luftsensor_data(args.year, args.sensor_type, args.sensor_id)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
