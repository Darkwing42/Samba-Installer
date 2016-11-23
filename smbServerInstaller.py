import subprocess


class Installer():
    pass


def InstallerCentOS():
    subprocess.call(["yum", "install", "samba", "samba-client", "samba-common"])
    
def InstallerDebian():
    subprocess.call(["apt-get", "install", "samba", "samba-client", "samba-common"])
