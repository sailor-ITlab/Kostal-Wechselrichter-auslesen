from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from functools import wraps
from waitress import serve
import threading
import datetime
from Wechselrichter.Wechselr_auslesen import Wechselr_Keller_auslesen
from Wechselrichter.Wechselr_auslesen import Wechselr_Gartenhaus_auslesen

class Solar():
    def __init__(self):
        # Variablen für definitione
        # Variablen für Übergabe mit Threads
        self.Wechselr_Keller_Werte = [None] * 2
        self.Wechselr_Gartenhaus_Werte = [None] * 2
        # Objekte erstellen
        print("starting pymodbus")
        self.Obj_Wechselr_Keller = Wechselr_Keller_auslesen.Wechselr_Keller()
        print("starting selenium/Firefox")
        self.Obj_Wechselr_Gartenhaus = Wechselr_Gartenhaus_auslesen.Wechselr_Gartenhaus()

    def Wechselr_Keller_auslesen(self):
        thr_Wechselr_Keller_auslesen = threading.Thread(target=self.Obj_Wechselr_Keller.auslesen, args=(None, self.Wechselr_Keller_Werte))
        thr_Wechselr_Keller_auslesen.start()
        thr_Wechselr_Keller_auslesen.join()
        return self.Wechselr_Keller_Werte

    def Wechselr_Gartenhaus_auslesen(self):
        thr_Wechselr_Gartenhaus_auslesen = threading.Thread(target=self.Obj_Wechselr_Gartenhaus.auslesen, args=(None, self.Wechselr_Gartenhaus_Werte))
        thr_Wechselr_Gartenhaus_auslesen.start()
        thr_Wechselr_Gartenhaus_auslesen.join()
        return self.Wechselr_Gartenhaus_Werte

class API():
    def auth_required(self, f):
        @wraps(f)
        def decorated(*args, **kwargs):
            auth = request.authorization
            if (auth and (self.anmeldedaten.get(auth.username) == auth.password)):
                # print(f" [{datetime.datetime.now()}]: Zugriff von {request.remote_addr} ERLAUBT.")
                return f(*args, **kwargs)
            else:
                print(f" [{datetime.datetime.now()}]: Zugriff von {request.remote_addr} VERWEIGERT.")
                return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})

        return decorated
    def __init__(self):
        self.anmeldedaten = {
            'dev': 'dev-key'
        }


        Obj_Solar = Solar()

        app = Flask(__name__)
        CORS(app, origins=['http://api.local:*', 'https://api.local:*', 'http://127.0.0.1:*', 'http://localhost:*'], supports_credentials=True)
        # CORS(app, origins=['*']) # Nur für Entwicklung verwenden, nicht für Produktion

        @app.route('/')
        @self.auth_required
        def flask_api_test():
            print(f" [{datetime.datetime.now()}]: Zugriff von {request.remote_addr} auf die API (/).")
            data = {
                'API launched successfully': 'True'
            }
            return jsonify(data), 200

        @app.route('/get-solardata-keller', methods=['GET'])
        @self.auth_required
        def get_solardata_keller():
            print(f" [{datetime.datetime.now()}]: Zugriff von {request.remote_addr} auf die API (/get-solardata-keller).")
            Wechselr_Keller_Werte = Obj_Solar.Wechselr_Keller_auslesen()
            # print(Wechselr_Keller_Werte)
            data = {
                'Zeitpunkt_Wechselr_Keller_auslesen': Wechselr_Keller_Werte[0],
                'Batterie_In_Output': float(Wechselr_Keller_Werte[1][23][4] * Wechselr_Keller_Werte[1][25][4]),
                'Batterie_Ladestand_Prozent': float(Wechselr_Keller_Werte[1][24][4]),
                'PV_Produktion_Keller': float(Wechselr_Keller_Werte[1][37][4] + Wechselr_Keller_Werte[1][38][4]),
                'Netz_In_Output': float(Wechselr_Keller_Werte[1][36][4])
            }
            return jsonify(data), 200

        @app.route('/get-solardata-gartenhaus', methods=['GET'])
        @self.auth_required
        def get_solardata_gartenhaus():
            print(f" [{datetime.datetime.now()}]: Zugriff von {request.remote_addr} auf die API (/get-solardata-gartenhaus).")
            Wechselr_Gartenhaus_Werte = Obj_Solar.Wechselr_Gartenhaus_auslesen()
            # Fehlervermeidung: Falls None oder '' als Wert gegeben diesen auf 0 setzen
            for i in range(len(Wechselr_Gartenhaus_Werte[1])):

                if (Wechselr_Gartenhaus_Werte[1][i][3] == None or Wechselr_Gartenhaus_Werte[1][i][3] == ''):
                    Wechselr_Gartenhaus_Werte[1][i][3] = float(0.0)
                else:
                    Wechselr_Gartenhaus_Werte[1][i][3] = float(Wechselr_Gartenhaus_Werte[1][i][3])

            # print(Wechselr_Gartenhaus_Werte)
            data = {
                'Zeitpunkt_Wechselr_Gartenhaus_auslesen': Wechselr_Gartenhaus_Werte[0],
                'PV_Produktion_Gartenhaus': float(Wechselr_Gartenhaus_Werte[1][3][3])
            }
            return jsonify(data), 200

        @app.route('/get-solardata-all', methods=['GET'])
        @self.auth_required
        def get_solardata_all():
            print(f" [{datetime.datetime.now()}]: Zugriff von {request.remote_addr} auf die API (/get-solardata-all).")
            Wechselr_Keller_Werte = Obj_Solar.Wechselr_Keller_auslesen()
            Wechselr_Gartenhaus_Werte = Obj_Solar.Wechselr_Gartenhaus_auslesen()
            # Fehlervermeidung: Falls None oder '' als Wert gegeben diesen auf 0 setzen
            for i in range(len(Wechselr_Gartenhaus_Werte[1])):

                if (Wechselr_Gartenhaus_Werte[1][i][3] == None or Wechselr_Gartenhaus_Werte[1][i][3] == ''):
                    Wechselr_Gartenhaus_Werte[1][i][3] = float(0.0)
                else:
                    Wechselr_Gartenhaus_Werte[1][i][3] = float(Wechselr_Gartenhaus_Werte[1][i][3])

            # print(Wechselr_Gartenhaus_Werte)
            data = {
                'Zeitpunkt_Wechselr_Keller_auslesen': Wechselr_Keller_Werte[0],
                'Zeitpunkt_Wechselr_Gartenhaus_auslesen': Wechselr_Gartenhaus_Werte[0],
                'Batterie_In_Output': float(Wechselr_Keller_Werte[1][23][4] * Wechselr_Keller_Werte[1][25][4]),
                'Batterie_Ladestand_Prozent': float(Wechselr_Keller_Werte[1][24][4]),
                'PV_Produktion_Keller': float(Wechselr_Keller_Werte[1][37][4] + Wechselr_Keller_Werte[1][38][4]),
                'PV_Produktion_Gartenhaus': float(Wechselr_Gartenhaus_Werte[1][3][3]),
                'PV_Produktion_Gesamt': float(Wechselr_Keller_Werte[1][37][4] + Wechselr_Keller_Werte[1][38][4] + Wechselr_Gartenhaus_Werte[1][3][3]),
                'Netz_In_Output': float(Wechselr_Keller_Werte[1][36][4]),
                'Hausverbrauch': float(Wechselr_Keller_Werte[1][36][4] + Wechselr_Keller_Werte[1][37][4] + Wechselr_Keller_Werte[1][38][4] + Wechselr_Gartenhaus_Werte[1][3][3] + Wechselr_Keller_Werte[1][23][4] * Wechselr_Keller_Werte[1][25][4])
            }
            return jsonify(data), 200

        # app.run(debug=False, host='0.0.0.0', port=8001)
        print("starting API")
        serve(app, host='0.0.0.0', port=8001)

Obj_API = API()