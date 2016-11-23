#!/usr/bin/python3

import smbConfCreater, distroCheck


distroCheck.osCheck() # Checkt die Linux Distribution



smbConfCreater.backupSmbConf() # Erstellt die Globale smb.conf


