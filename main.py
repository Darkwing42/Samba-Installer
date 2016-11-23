#!/usr/bin/python3

import smbConfCreater, distroCheck



distroCheck.osCheck() # Prüft welche Linux Distribution installiert ist.



smbConfCreater.backupSmbConf() # Erstellt die Globale smb.conf und macht ein Backup von der Vorhandenen.


