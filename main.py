import os, subprocess, platform, sys


import smbConfCreater, distroCheck


distroCheck.osCheck() # Checkt die Linux Distribution

smbConfCreater.ConfCreater() # Erstellt die Globale smb.conf

