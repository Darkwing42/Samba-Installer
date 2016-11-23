#Erstellt die normale smb.conf Datei


import os, os.path, shutil

class smbConfCreater():
    pass


#Prüfung ob die Conf-Datei existiert
def backupSmbConf():
    path = "/etc/samba/smb.conf"
    
    if os.path.exists(path) == True:
        print("Die smb.conf Datei existiert bereits. Erstelle Backup........\n")
        shutil.move(path, "/etc/samba/smb.conf.bak")
        print("Backup erstellt. Neue smb.conf Datei wird generiert.\n")
        ConfCreater()
    elif os.path.exists(path) == False:
        print("Generiere neue smb.conf Datei.....\n")
        ConfCreater()

    
#Globalen Parameter für die Conf-Datei
def ConfCreater():
    serverName = input("Unter welcher Bezeichnung soll der Server im Netzwerk zu finden sein?\n")
    workgroup = input("In welcher WORKGROUP befindet sich der Server?")
    workgroup = workgroup.upper()
    openFile = open("/etc/samba/smb.conf", "w+")
    openFile.write("[global]\n")
    openFile.write("workgroup = "+ workgroup + "\n")
    openFile.write("server string = Samba Server %v\n")
    openFile.write("netbios name = " + serverName + "\n")
    openFile.write("security = user\n")
    openFile.write("map to guest = bad user\n")
    openFile.write("dns proxy = no\n")
    openFile.write("#========================================Share Definition====================================\n")
    openFile.close()
    
    
