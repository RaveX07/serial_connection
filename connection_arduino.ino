void get_data(){
    // wenn keine seriellen Daten --> beende Funktion
    if(Serial.available() <= 0){
        return;
    }

    // Wenn serielle Daten verfügbar --> lese bis Zeilenumbruch (Ende)
    String data = Serial.readStringUntil('\n');

    // mach irgendwas mit String
}

void setup() {
    // Initialisieren der seriellen Verbindung
    Serial.begin(115200);
    Serial.setTimeout(5);
}

void loop() {
    getData();      // warten auf Nachricht
}
