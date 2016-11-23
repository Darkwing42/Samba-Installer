import os, sys 


class Installer():
    pass


def InstallerCentOS():
    retcode = os.system("yum install samba samba-client samba-common")
    if retcode == 0:
        pass
    else:
        print("Fehler wurde erkannt. Installation wird abgebrochen!\n")
        input("")
        sys.exit()
    
    
def InstallerDebian():
    retcode = os.system("apt-get install samba samba-client samba-common")
    if retcode == 0:
        pass
    else:
        print("Fehler wurde erkannt. Installation wird abgebrochen!\n")
        input("")
        sys.exit()
