#! /usr/bin/python
import sys
import os
from subprocess import getoutput
def check_dependente():
    adb = getoutput("which adb")
    gradle = getoutput("which gradle")
    android-sdk = getoutput("which adb")
    adb = getoutput("which adb")
    

def sshinstall(util):
    if sys.platform == 'win*':
        clear()
        try:
         os.system("scoop install <service>")
        except:
            print("scoop not installed")
            os.system("""""")
            sshinstall()
    else:
        clear()
        apt = ['debian', 'ubuntu']
        yum = ['centos']
        dnf = ['fedora']
        pacman = ['arch', ]
        rpm = []
        emerge = ['gentoo']
        distr = definedistr()
        if distr in apt:
            os.system('apt update -y')
            os.system('apt install openssh-server -y')
        elif distr in yum:
            pass
        elif distr in dnf:
            os.system("dnf update")
            os.system('dnf install openssh-server -y')
        elif distr in pacman:
            os.system('pacman -Sy')
            os.system('pacman -S openssh')
        elif distr in rpm:
            os.system("rpm update")
            os.system('rpm install ')
        elif distr in emerge:
            os.system('emerge --sync')
            os.system('emerge openssh')
        else:
            menu()


def main():
    pass


if __name__ == '__main__':
    main()
