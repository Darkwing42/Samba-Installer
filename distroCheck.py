#Checkt welche Linux Distribution installiert ist


import platform, sys, smbServerInstaller

class distroCheck():
    pass


def osCheck():
    debianOS = ("Debian", "", "")
    #antergosOS = ("Antergos Linux", "", "")
    centOS = ("CentOs Linux", "", "")
    
    global osCheck
    osCheck = platform.linux_distribution()
    
    for osType in debianOS:
        debianOSLower = debianOS[0].lower()
        break
    
    #for osType in antergosOS:
    #    antergosOSLower = antergosOS[0].lower()
    #    break
    
    for osType in centOS:
        centOSLower = centOS[0].lower()
        break
    for osType in osCheck:
        osCheckLower = osCheck[0].lower()
        break
    
    if osCheckLower == debianOSLower:
        print("Debian gefunden.... Fahre fort!\n")
       retcode =  smbServerInstaller.InstallerDebian()
       if retcode == 0:
           pass
       else:
        print("Fehler kein Betriebsystem erkannt!\n")
        print("Programm wird beendet!\n")
        input("\n")
        sys.exit()    
            
        
    #elif osCheckLower == antergosOSLower:
    #    print("Antergos gefunden.... Fahre fort!\n")
    elif osCheckLower == centOSLower:
        print("CentOs gefunden.... Fahre fort!\n")
        retcode = smbServerInstaller.InstallerCentOS()
        if retcode == 0:
            pass
        else:
            print("Fehler kein Betriebsystem erkannt!\n")
            print("Programm wird beendet!\n")
            input("\n")
            sys.exit()

        










