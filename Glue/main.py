# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import DataCrawler
import PythonShell
import PythonShellETL

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # DataCrawler.create_crawler()
    # DataCrawler.start_crawler()
    ip_list = ['122.129.85.136'] #, '203.130.20.136', '116.58.46.176']
    #PythonShell.get_location(ip_list)
    PythonShellETL.get_location()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
