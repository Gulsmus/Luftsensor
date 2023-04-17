# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from Scripts.luftsensor_download import LuftsensorDownload
import argparse

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.

def get_luftsensor_data(year, sensor_type, sensor_id):
    luftsensor_data = LuftsensorDownload()
    if luftsensor_data.check_database(year, sensor_id):
        luftsensor_data.visualize_luftsensor_data(year, sensor_id)
    else:
        luftsensor_data.download_data(year, sensor_type, sensor_id)
        luftsensor_data.visualize_luftsensor_data(year, sensor_id)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #test = LuftsensorDownload()
    #test.download_data(year=2022,sensor_type="sds011",data_id="3280")
    #test.import_to_database()
    #test.visualize_luftsensor_data(3280)

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
