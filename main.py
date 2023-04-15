# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from Scripts.luftsensor_download import LuftsensorDownload

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')
    test = LuftsensorDownload()
    #test.download_data(year=2022,sensor_type="sds011",data_id="3280")
    #test.import_to_database()
    test.visualize_luftsensor_data(3280)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
