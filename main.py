#!/usr/bin/python3

import smbConfCreater, distroCheck, SharingRE


distroCheck.osCheck() # Prüft welche Linux Distribution installiert ist.



smbConfCreater.backupSmbConf() # Erstellt die Globale smb.conf und macht ein Backup von der Vorhandenen.


#Abfrage welche Art von Server installiert werden soll.
print("Welche Art Samba-Server soll installiert werden?\n")
eingabe = input("Read-Only, Anonymous(mit anonymen Schreibrechten, Secure Server?\n")
eingabe = eingabe.lower()


if eingabe == "read-only":
    SharingRE.shareDefinitionReadOnly()
    
#elif eingabe == "anonymous":

#elif eingabe == "secure server":
