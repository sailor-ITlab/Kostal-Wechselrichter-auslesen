import datetime
def Werte_verrechnen(Wechselr_Keller_Werte, Wechselr_Gartenhaus_Werte, Wechselr_Werte_verrechnet):
    # Benötigte Werte:
    """
    X Batterie_In_Output
    X Batterie_Ladestand_Prozent
    X PV_Produktion_Keller
    X PV_Produktion_Gartenhaus
    X PV_Produktion_Gesamt
    X Netz_In_Output
    X Hausverbrauch
    """

    # Fehlervermeidung: Falls None oder '' als Wert gegeben diesen auf 0 setzen
    for i in range(len(Wechselr_Gartenhaus_Werte[1])):

        if(Wechselr_Gartenhaus_Werte[1][i][3] == None or Wechselr_Gartenhaus_Werte[1][i][3] == ''):
            Wechselr_Gartenhaus_Werte[1][i][3] = float(0.0)
        else:
            Wechselr_Gartenhaus_Werte[1][i][3] = float(Wechselr_Gartenhaus_Werte[1][i][3])

    # Werte verrechnen bzw. in eindeutige Variablen schreiben

    # --------- Batterie Werte(an wechselr Keller)
    # ... = Actual battery charge (-) / discharge (+) current(200) * Battery voltage(216)
    Batterie_In_Output = float(Wechselr_Keller_Werte[1][23][4] * Wechselr_Keller_Werte[1][25][4])
    # ... = Act. state of charge(210)
    Batterie_Ladestand_Prozent = float(Wechselr_Keller_Werte[1][24][4])


    # --------- PV Werte Keller (an wechselr Keller)
    # ... = Power DC1(260) + Power DC2(270)
    PV_Produktion_Keller = float(Wechselr_Keller_Werte[1][37][4] + Wechselr_Keller_Werte[1][38][4])


    # --------- PV Werte Gartenhaus (an wechselr Gartenhaus)
    # ... = AC Power_fast
    PV_Produktion_Gartenhaus = float(Wechselr_Gartenhaus_Werte[1][3][3])

    # --------- PV Werte Beide (an beiden wechselr)
    # ... [{Power DC1(260) + Power DC2(270)} wechselr Keller] + [{AC Power_fast} wechselr Gartenhaus]
    PV_Produktion_Gesamt = float(PV_Produktion_Keller + PV_Produktion_Gartenhaus)

    # --------- Netz Werte (Powermeter über wechselr Keller)
    # ... = Total active power (powermeter)(252)
    Netz_In_Output = float(Wechselr_Keller_Werte[1][36][4])


    # --------- Hausverbrauch Werte (beide Wechselr)
    # ... = Netz_In_Output + PV_Produktion_Gesamt + Batterie_In_Output
    Hausverbrauch = float(Netz_In_Output + PV_Produktion_Gesamt + Batterie_In_Output)


    print('     Batterie_In_Output:', Batterie_In_Output)
    print('     Batterie_Ladestand_Prozent:', Batterie_Ladestand_Prozent)
    # PV Keller
    print('     PV_Produktion_Keller:', PV_Produktion_Keller)
    # PV Gartenhaus
    print('     PV_Produktion_Gartenhaus:', PV_Produktion_Gartenhaus)
    # # PV Beide
    print('     PV_Produktion_Gesamt:', PV_Produktion_Gesamt)
    # Netz
    print('     Netz_In_Output:', Netz_In_Output)
    # Hausverbrauch
    print('     Hausverbrauch:', Hausverbrauch)


    Wechselr_Werte_verrechnet[0] = [Wechselr_Keller_Werte[0], Wechselr_Gartenhaus_Werte[0], ['Batterie_In_Output', Batterie_In_Output], ['Batterie_Ladestand_Prozent', Batterie_Ladestand_Prozent], ['PV_Produktion_Keller', PV_Produktion_Keller], ['PV_Produktion_Gartenhaus', PV_Produktion_Gartenhaus], ['PV_Produktion_Gesamt', PV_Produktion_Gesamt], ['Netz_In_Output', Netz_In_Output], ['Hausverbrauch', Hausverbrauch]]
