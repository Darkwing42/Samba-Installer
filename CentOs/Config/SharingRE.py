#Read Only Konfiguration


import os

class ReadOnly():
    pass

def shareReadOnly():
    path = "/etc/samba/smb.conf"
    openFile = open(path, "a")
    
    nameShare = input("Name der Freigabe?\n")
    pathShare = input("Ordner der Samba Freigabe? \n")
    browsable = input("Soll die Freigabe durchsuchbar sein? y/n....\n")
    browsable = browsable.lower()
    writable = input("Soll die Freigabe beschreibbar sein? y/n....\n")
    writable = writable.lower()
    guestOk = input("Guest Ok? y/n....\n")
    guestOk = guestOk.lower()
    readOnly = input("Read-Only? y/n...\n")
    readOnly = readOnly.lower()
    
    openFile.write("[" + nameShare + "]")
    openFile.write(pathShare)
    
    if browsable == "y":
        openFile.write("browsable = yes")
    elif browsable == "n":
        openFile.write("browsable = no")
    else:
        print("Browsable: Klappt nicht!")
        
    if writable == "y":
        openFile.write("writable = yes")
    elif writable == "n":
        openFile.write("writable = no")
    else:
        print("writable: Klappt nicht!")
    
    if guestOk == "y":
        openFile.write("guest ok = yes")
    elif guestOk == "n":
        openFile.write("guest ok = no")
    else:
        print("Guest ok: Klappt nicht!")
        
    if readOnly == "y":
        openFile.write("read only = yes")
    elif readOnly == "n":
        openFile.write("read only = no")
    else:
        print("Read Only: Klappt nicht")
        
    openFile.close()
        
    
        
    
    
