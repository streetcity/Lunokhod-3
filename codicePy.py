import serial  #comunicazione seriale
import time    #gestire il tempo 

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1) #Crea connessione seriale sull'interfaccia 

file_path = "dati_temperatura.csv" #Definisce percorso e nome del file CSV dove salviamo i dati

print("Inizio acquisizione dati (Ctrl+C per fermare)") #Messaggio iniziale per informare l'utente

try:
    while True:  # Loop infinito finché non viene interrotto manualmente
        linea = ser.readline().decode('utf-8').strip()  #Legge riga da seriale, decodifica e rimuove spazi inutili
        if linea:  #no vuota
            ora = time.strftime("%Y-%m-%d %H:%M:%S")
            dato = f"{ora},{linea}\n"  # Prepara dato da salvare nel formato "timestamp,valore"
            print(dato.strip())  #Stampa dato senza ritorno a capo aggiuntivo
            with open(file_path, "a") as file:  #Apre il file in modalità append ("a" = aggiunta dati)
                file.write(dato)  #Scrive il dato nel file
except KeyboardInterrupt:  #Se l'utente preme Ctrl+C
    print("\nAcquisizione terminata.")  #Messaggio di chiusura
    ser.close()  # Chiude correttamente la connessione seriale
