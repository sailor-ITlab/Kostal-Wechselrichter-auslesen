# pymodbus getestet mit Version 2.5.3
import datetime
from pymodbus.client.sync import ModbusTcpClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder

class Wechselr_Keller():
    def __init__(self):
        # Programm orientiert an Copyright (C) 2018  Kilian Knoll
        # Bechreibung zum auslesen und welche ID was ist unter:
        #       https://www.kostal-solar-electric.com/de-de/download/download/#Solar-Wechselrichter/PLENTICORE%20plus/Deutschland/Schnittstellen%20Protokolle/Schnitstellen Protokolle

        self.IP_Wechselrichter_Keller = '172.16.10.37'
        self.Port_Wechselrichter_Keller = '1502'

        self.Werte = []


        # Aufbau Adr Variablen: Adr5 = [Adresse im Wechselrichter, Beschreibung von Kostal, Datentyp im Wechselrichter, Einheit, Wert]

        # 0
        Adr98 = [98]
        Adr98.append('Temperature of controller PCB')
        Adr98.append('Float')
        Adr98.append('°C')
        # print(Adr98)
        self.Werte.append(Adr98)

        # 1
        Adr100 = [100]
        Adr100.append('Total DC power')
        Adr100.append('Float')
        Adr100.append('W')
        # print('Total DC power', Adr100)
        self.Werte.append(Adr100)

        # 2
        Adr106 = [106]
        Adr106.append('Home own consumption from battery')
        Adr106.append('Float')
        Adr106.append('W')
        # print(Adr106)
        self.Werte.append(Adr106)

        # 3
        Adr108 = [108]
        Adr108.append('Home own consumption from grid ')
        Adr108.append('Float')
        Adr108.append('W')
        # print(Adr108)
        self.Werte.append(Adr108)

        # 4
        Adr110 = [110]
        Adr110.append('Total home consumption Battery ')
        Adr110.append('Float')
        Adr110.append('Wh')
        # print(Adr110)
        self.Werte.append(Adr110)

        # 5
        Adr112 = [112]
        Adr112.append('Total home consumption Grid')
        Adr112.append('Float')
        Adr112.append('Wh')
        # print(Adr112)
        self.Werte.append(Adr112)

        # 6
        Adr114 = [114]
        Adr114.append('Total home consumption PV')
        Adr114.append('Float')
        Adr114.append('Wh')
        # print('Total home consumption PV', Adr114)
        self.Werte.append(Adr114)

        # 7
        Adr116 = [116]
        Adr116.append('Home own consumption from PV')
        Adr116.append('Float')
        Adr116.append('W')
        # print('Home own consumption from PV', Adr116)
        self.Werte.append(Adr116)

        # 8
        Adr118 = [118]
        Adr118.append('Total home consumption')
        Adr118.append('Float')
        Adr118.append('Wh')
        # print(Adr118)
        self.Werte.append(Adr118)

        # 9
        Adr124 = [124]
        Adr124.append('Total home consumption rate')
        Adr124.append('Float')
        Adr124.append('%')
        # print(Adr124)
        self.Werte.append(Adr124)

        # 10
        Adr152 = [152]
        Adr152.append('Grid frequency')
        Adr152.append('Float')
        Adr152.append('Hz')
        # print(Adr152)
        self.Werte.append(Adr152)

        # 11
        Adr154 = [154]
        Adr154.append('Current Phase 1')
        Adr154.append('Float')
        Adr154.append('A')
        # print(Adr154)
        self.Werte.append(Adr154)

        # 12
        Adr156 = [156]
        Adr156.append('Active power Phase 1')
        Adr156.append('Float')
        Adr156.append('W')
        # print(Adr156)
        self.Werte.append(Adr156)

        # 13
        Adr158 = [158]
        Adr158.append('Voltage Phase 1')
        Adr158.append('Float')
        Adr158.append('V')
        # print(Adr158)
        self.Werte.append(Adr158)

        # 14
        Adr160 = [160]
        Adr160.append('Current Phase 2')
        Adr160.append('Float')
        Adr160.append('A')
        # print(Adr160)
        self.Werte.append(Adr160)

        # 15
        Adr162 = [162]
        Adr162.append('Active power Phase 2')
        Adr162.append('Float')
        Adr162.append('W')
        # print(Adr162)
        self.Werte.append(Adr162)

        # 16
        Adr164 = [164]
        Adr164.append('Voltage Phase 2')
        Adr164.append('Float')
        Adr164.append('V')
        # print(Adr164)
        self.Werte.append(Adr164)

        # 17
        Adr166 = [166]
        Adr166.append('Current Phase 3')
        Adr166.append('Float')
        Adr166.append('A')
        # print(Adr166)
        self.Werte.append(Adr166)

        # 18
        Adr168 = [168]
        Adr168.append('Active power Phase 3')
        Adr168.append('Float')
        Adr168.append('W')
        # print(Adr168)
        self.Werte.append(Adr168)

        # 19
        Adr170 = [170]
        Adr170.append('Voltage Phase 3')
        Adr170.append('Float')
        Adr170.append('V')
        # print(Adr170)
        self.Werte.append(Adr170)

        # 20
        Adr172 = [172]
        Adr172.append('Total AC active power')
        Adr172.append('Float')
        Adr172.append('W')
        # print('Total AC active power', Adr172)
        self.Werte.append(Adr172)

        # 21
        Adr190 = [190]
        Adr190.append('Battery charge current ')
        Adr190.append('Float')
        Adr190.append('A')
        # print(Adr190)
        self.Werte.append(Adr190)

        # 22
        Adr194 = [194]
        Adr194.append('Number of battery cycles')
        Adr194.append('Float')
        Adr194.append('-')
        # print(Adr194)
        self.Werte.append(Adr194)

        # 23
        Adr200 = [200]
        Adr200.append('Actual battery charge (-) / discharge (+) current')
        Adr200.append('Float')
        Adr200.append('A')
        # print(Adr200)
        self.Werte.append(Adr200)

        # 24
        Adr210 = [210]
        Adr210.append('Act. state of charge')
        Adr210.append('Float')
        Adr210.append('%')
        # print(Adr210)
        self.Werte.append(Adr210)

        # 25
        Adr216 = [216]
        Adr216.append('Battery voltage')
        Adr216.append('Float')
        Adr216.append('V')
        # print(Adr216)
        self.Werte.append(Adr216)

        # 26
        Adr220 = [220]
        Adr220.append('Frequency (powermeter)')
        Adr220.append('Float')
        Adr220.append('Hz')
        # print(Adr220)
        self.Werte.append(Adr220)

        # 27
        Adr222 = [222]
        Adr222.append('Current phase 1 (powermeter)')
        Adr222.append('Float')
        Adr222.append('A')
        # print(Adr222)
        self.Werte.append(Adr222)

        # 28
        Adr224 = [224]
        Adr224.append('Active power phase 1 (powermeter)')
        Adr224.append('Float')
        Adr224.append('W')
        # print('Active power phase 1 (powermeter)', Adr224)
        self.Werte.append(Adr224)

        # 29
        Adr230 = [230]
        Adr230.append('Voltage phase 1 (powermeter)')
        Adr230.append('Float')
        Adr230.append('V')
        # print(Adr230)
        self.Werte.append(Adr230)

        # 30
        Adr232 = [232]
        Adr232.append('Current phase 2 (powermeter)')
        Adr232.append('Float')
        Adr232.append('A')
        # print(Adr232)
        self.Werte.append(Adr232)

        # 31
        Adr234 = [234]
        Adr234.append('Active power phase 2 (powermeter)')
        Adr234.append('Float')
        Adr234.append('W')
        # print('Active power phase 2 (powermeter)', Adr234)
        self.Werte.append(Adr234)

        # 32
        Adr240 = [240]
        Adr240.append('Voltage phase 2 (powermeter) ')
        Adr240.append('Float')
        Adr240.append('V')
        # print(Adr240)
        self.Werte.append(Adr240)

        # 33
        Adr242 = [242]
        Adr242.append('Current phase 3 (powermeter)')
        Adr242.append('Float')
        Adr242.append('A')
        # print(Adr242)
        self.Werte.append(Adr242)

        # 34
        Adr244 = [244]
        Adr244.append('Active power phase 3 (powermeter)')
        Adr244.append('Float')
        Adr244.append('W')
        # print('Active power phase 3 (powermeter)', Adr244)
        self.Werte.append(Adr244)

        # 35
        Adr250 = [250]
        Adr250.append('Voltage phase 3 (powermeter)')
        Adr250.append('Float')
        Adr250.append('W')
        # print(Adr250)
        self.Werte.append(Adr250)

        # 36
        Adr252 = [252]
        Adr252.append('Total active power (powermeter)')
        # Sensor position 1 (home consumption): (+) House consumption, (-) generation
        # Sensor position 2 (grid connection): (+) Power supply, (-) feed - in
        Adr252.append('Float')
        Adr252.append('W')
        # print('Total active power (powermeter)', Adr252)
        self.Werte.append(Adr252)

        # 37
        Adr260 = [260]
        Adr260.append('Power DC1')
        Adr260.append('Float')
        Adr260.append('W')
        # print(Adr260)
        self.Werte.append(Adr260)

        # 38
        Adr270 = [270]
        Adr270.append('Power DC2')
        Adr270.append('Float')
        Adr270.append('W')
        # print(Adr270)
        self.Werte.append(Adr270)

        # 39
        Adr280 = [280]
        Adr280.append('Power DC3')
        Adr280.append('Float')
        Adr280.append('W')
        # print(Adr280)
        self.Werte.append(Adr280)

        # 40
        Adr320 = [320]
        Adr320.append('Total yield')
        Adr320.append('Float')
        Adr320.append('Wh')
        # print(Adr320)
        self.Werte.append(Adr320)

        # 41
        Adr322 = [322]
        Adr322.append('Daily yield')
        Adr322.append('Float')
        Adr322.append('Wh')
        # print(Adr322)
        self.Werte.append(Adr322)

        # 42
        Adr324 = [324]
        Adr324.append('Yearly yield')
        Adr324.append('Float')
        Adr324.append('Wh')
        # print(Adr324)
        self.Werte.append(Adr324)

        # 43
        Adr326 = [326]
        Adr326.append('Monthly yield')
        Adr326.append('Float')
        Adr326.append('Wh')
        # print(Adr326)
        self.Werte.append(Adr326)

        # 44
        Adr575 = [575]
        Adr575.append('Inverter Generation Power (actual)')
        Adr575.append('S16')
        Adr575.append('W')
        # print('Inverter Generation Power (actual)', Adr575)
        self.Werte.append(Adr575)

        # 45
        Adr577 = [577]
        Adr577.append('Generation Energy')
        Adr577.append('U32')
        Adr577.append('Wh')
        # print('Generation Energy', Adr577)
        self.Werte.append(Adr577)

        for i in range(len(self.Werte)):
            self.Werte[i].append(0)

    # ----------------------------------------- Quelle für Read-Funktionen: Copyright (C) 2018  Kilian Knoll
    # Routine to read a string from one address with 8 registers
    def ReadStr8(self, myadr_dec):
        r1 = self.client.read_holding_registers(myadr_dec, 8, unit=71)
        STRG8Register = BinaryPayloadDecoder.fromRegisters(r1.registers, byteorder=Endian.Big)
        result_STRG8Register = STRG8Register.decode_string(8)
        return (result_STRG8Register)
        # -----------------------------------------

    # Routine to read a Float from one address with 2 registers
    def ReadFloat(self, myadr_dec):
        r1 = self.client.read_holding_registers(myadr_dec, 2, unit=71)
        FloatRegister = BinaryPayloadDecoder.fromRegisters(r1.registers, byteorder=Endian.Big,
                                                               wordorder=Endian.Little)
        result_FloatRegister = round(FloatRegister.decode_32bit_float(), 2)
        return (result_FloatRegister)
            # -----------------------------------------

    # Routine to read a U16 from one address with 1 register
    def ReadU16_1(self, myadr_dec):
        r1 = self.client.read_holding_registers(myadr_dec, 1, unit=71)
        U16register = BinaryPayloadDecoder.fromRegisters(r1.registers, byteorder=Endian.Big, wordorder=Endian.Little)
        result_U16register = U16register.decode_16bit_uint()
        return (result_U16register)

    # Routine to read a U16 from one address with 2 registers
    def ReadU16_2(self, myadr_dec):
        r1 = self.client.read_holding_registers(myadr_dec, 2, unit=71)
        U16register = BinaryPayloadDecoder.fromRegisters(r1.registers, byteorder=Endian.Big, wordorder=Endian.Little)
        result_U16register = U16register.decode_16bit_uint()
        return (result_U16register)

    # Routine to read a U32 from one address with 2 registers
    def ReadU32(self, myadr_dec):
        r1 = self.client.read_holding_registers(myadr_dec, 8, unit=71)
        U32register = BinaryPayloadDecoder.fromRegisters(r1.registers, byteorder=Endian.Big, wordorder=Endian.Little)
        result_U32register = U32register.decode_32bit_uint()
        return (result_U32register)

    # Routine to read a U32 from one address with 2 registers
    def ReadS16(self, myadr_dec):
        r1 = self.client.read_holding_registers(myadr_dec, 1, unit=71)
        S16register = BinaryPayloadDecoder.fromRegisters(r1.registers, byteorder=Endian.Big, wordorder=Endian.Little)
        result_S16register = S16register.decode_16bit_uint()
        return (result_S16register)
    # -----------------------------------------

    def auslesen(self, unnoetig, Werte_Wechselr_Keller):
        self.client = ModbusTcpClient(host=self.IP_Wechselrichter_Keller, port=self.Port_Wechselrichter_Keller)
        self.client.connect()

        for i in range(len(self.Werte)):
            if(self.Werte[i][2] == 'Float'):
                self.Werte[i][4] = self.ReadFloat(self.Werte[i][0])
            elif(self.Werte[i][2] == 'S16'):
                self.Werte[i][4] = self.ReadS16(self.Werte[i][0])
            elif (self.Werte[i][2] == 'U32'):
                self.Werte[i][4] = self.ReadU32(self.Werte[i][0])
            else:
                print('Wert kann nicht ausgelesen werden: FALL NICHT PROGRAMMIERT')

        Werte_Wechselr_Keller[0] = datetime.datetime.now()
        Werte_Wechselr_Keller[1] = self.Werte
