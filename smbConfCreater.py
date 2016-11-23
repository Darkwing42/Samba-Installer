#Erstellt die normale smb.conf Datei


import os
class smbConfCreater():
    pass

def ConfCreater():
    serverName = input("Unter welcher Bezeichnung soll der Server im Netzwerk zu finden sein?\n")
    openFile = open("/etc/samba/smb.conf", "w+")
    openFile.write("[global]\n")
    openFile.write("server string = Samba Server %v\n")
    openFile.write("netbios name = " + serverName + "\n")
    openFile.write("security = user\n")
    openFile.write("map to guest = bad user\n")
    openFile.write("dns proxy = no\n")
    openFile.write("#========================================Share Definition====================================\n")
    openFile.close()
    
    
