from Config import SharingRE

class AbfrageCentOs():
    pass

def abfrageCentOs():
    
    #Abfrage welche Art von Server installiert werden soll.
    print("Welche Art Samba-Server soll installiert werden?\n")
    eingabe = input("Read-Only, Anonymous(mit anonymen Schreibrechten, Secure Server?\n")
    eingabe = eingabe.lower()


    if eingabe == "read-only":
   SharingRE.shareDefinitionReadOnly()
    
    #elif eingabe == "anonymous":

    #elif eingabe == "secure server":
