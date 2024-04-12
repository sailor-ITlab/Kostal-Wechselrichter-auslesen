from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import datetime
import time

class Wechselr_Gartenhaus:
    def __init__(self):
        # Set up Firefox options
        firefox_options = Options()
        firefox_options.add_argument('--headless')  # Run Firefox in headless mode
        # Set up the Firefox driver
        self.driver = webdriver.Firefox(options=firefox_options)
        # self.driver = webdriver.Firefox() # falls mit GUI getestet werden muss
        self.driver.get('http://172.16.10.36/pages/livechart.html')

        time.sleep(0.25)  # da sonst die Website nicht komplett geladen bzw. es funktioniert nicht

        self.Werte = []
        # Aufbau: AC_Voltage = [Name der ID im JS Code, Text auf Website, Einheit, Wert]
        # 0
        value0 = ['valueId0']
        value0.append('AC Voltage')
        value0.append('V')
        self.Werte.append(value0)

        # 1
        value1 = ['valueId1']
        value1.append('AC Current')
        value1.append('A')
        self.Werte.append(value1)

        # 2
        value2 = ['valueId2']
        value2.append('AC Power')
        value2.append('W')
        self.Werte.append(value2)

        # 3
        value3 = ['valueId3']
        value3.append('AC Power_fast')
        value3.append('W')
        self.Werte.append(value3)

        # 4
        value4 = ['valueId4']
        value4.append('AC Frequency')
        value4.append('Hz')
        self.Werte.append(value4)

        # 5
        value5 = ['valueId5']
        value5.append('DC Voltage1')
        value5.append('V')
        self.Werte.append(value5)

        # 6
        value6 = ['valueId6']
        value6.append('DC Voltage2')
        value6.append('V')
        self.Werte.append(value6)

        # 7
        value7 = ['valueId7']
        value7.append('DC Current1')
        value7.append('A')
        self.Werte.append(value7)

        # 8
        value8 = ['valueId8']
        value8.append('DC Current2')
        value8.append('A')
        self.Werte.append(value8)

        # 9
        value9 = ['valueId9']
        value9.append('LINK Voltage')
        value9.append('V')
        self.Werte.append(value9)

        # ungenutzt / keine Werte vorhanden

        # 10
        value10 = ['valueId10']
        value10.append('GridPower')
        value10.append('W')
        self.Werte.append(value10)

        # 11
        value11 = ['valueId11']
        value11.append('GridConsumedPower')
        value11.append('W')
        self.Werte.append(value11)

        # 12
        value12 = ['valueId12']
        value12.append('GridInjectedPower')
        value12.append('W')
        self.Werte.append(value12)

        # 13
        value13 = ['valueId13']
        value13.append('OwnConsumedPower')
        value13.append('W')
        self.Werte.append(value13)

        # Wert vorhanden, weiß nicht von was

        # 14
        value14 = ['valueId14']
        value14.append('Derating')
        value14.append('%')
        self.Werte.append(value14)

        for i in range(len(self.Werte)):
            self.Werte[i].append(0)

    def readByID(self, Id):
        # print('def read')
        value = self.driver.find_element(By.ID, Id).text
        # print(Value)
        return value

    def auslesen(self, unnoetig, Werte_Wechselr_Gartenhaus):
        for i in range(len(self.Werte)):
            self.Werte[i][3] = self.readByID(self.Werte[i][0])
        Werte_Wechselr_Gartenhaus[0] = datetime.datetime.now()
        Werte_Wechselr_Gartenhaus[1] = self.Werte

    def quit(self):
        self.driver.quit()

