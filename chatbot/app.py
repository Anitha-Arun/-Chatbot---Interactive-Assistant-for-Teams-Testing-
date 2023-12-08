from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

class Norden:
         
    def __init__ (self):
                self.greetings = ["hello", "hi", "hey","hello norden"]
                self.goodbyes = ["bye", "goodbye","thank you","tq","thanks","exit","quit","end"]
                self.responses = {
                    "hello": "Hi there! How can I help you?",
                    "hi": "Hello! What can I do for you?",
                    "hey": "Hey! How can I assist you today?",
                    "bye": "Goodbye! Have a great day!",
                    "goodbye": "See you later! Take care!",
                    "hello norden": "hi! my friend how can i help u",
                    "tq":"it's okay ",
                    "thanks":"Welcome ! ",
                    "thank you":"okay ! See you again", 
                    "exit":"bye see you soon",
                    "quit":"End",
                    "end":"End"}
        
    def connect(self):
                self.con=["how to connect adb","adb connect","connect adb","connect the devices"]
                self.responses={
                    "how to connect adb":"<b>Open CMD  </b><br> use this command  <br>adb connect <-ip address of the device-> <br> <i>note: remove <ip address of the device> and give IP</i>",
                    "adb connect":"<b>Open CMD  </b><br> use this command  <br> adb connect <-ip address of the device-><br> <i>note: remove <ip address of the device> and give IP</i>",
                    "connect the devices":"<b>Open CMD  </b><br> use this command  <br><b> adb connect <-ip address of the device-></b><br> <i>note: remove <ip address of the device> and give IP</i>",
                    "connect adb":"<b>Open CMD  </b><br> use this command  <br> adb connect <-ip address of the device-><br> <i>note: remove <ip address of the device> and give IP</i>"
                }

    def clear(self):
                self.c=["clear commands","clear cache commands","clear teams cache"]
                self.u=["unistall commands list","unistall teams commands ","unistall teams","unistall cp","unistall admin adgent"]
                self.responses={ 
                   "clear commands":''' <b> first connect to ADB to run!!  </b> <br>                                 
                    To clear cache for device <br><b>
                 Step </b>:adb shell pm clear com.microsoft.skype.teams.ipphone<br>
                        adb shell pm clear com.microsoft.windowsintune.companyportal<br>
                        adb shell pm clear com.microsoft.teams.ipphone.admin.agent<br><i>
                    Note::1.if u are connect more devices use -s after adb typed eg:adb -s <ip></i>''',
                    "clear cache commands":"""<b> first connect to ADB to run!!  </b> <br>                                 
                    To clear cache for device <br><b>
                 Step </b>:adb shell pm clear com.microsoft.skype.teams.ipphone<br>
                        adb shell pm clear com.microsoft.windowsintune.companyportal<br>
                        adb shell pm clear com.microsoft.teams.ipphone.admin.agent<br><i>
                    Note::1.if u are connect more devices use -s after adb typed eg:adb -s <ip></i>""",
                    "clear teams cache":"""  <b> first connect to ADB to run!!  </b> <br>                                 
                    To clear cache for device <br><b>
                 Step </b>:adb shell pm clear com.microsoft.skype.teams.ipphone<br>
                        adb shell pm clear com.microsoft.windowsintune.companyportal<br>
                        adb shell pm clear com.microsoft.teams.ipphone.admin.agent<br><i>
                    Note::1.if u are connect more devices use -s after adb typed eg:adb -s <ip></i>""",

                    #unistall
                    "unistall commands list":""" <b>first connect to ADB to run !! </b><br>
                        adb shell pm uninstall com.microsoft.windowsintune.companyportal<br>
                        adb shell pm uninstall com.microsoft.skype.teams.ipphone<br>
                        adb uninstall com.microsoft.teams.ipphone.admin.agent<br><i>
                        note:1.if u are connect more devices use -s after adb typed eg:adb -s <ip></i>""",
                    "unistall teams commands ":""" <b>first connect to ADB to run !! </b><br>
                        adb shell pm uninstall com.microsoft.windowsintune.companyportal<br>
                        adb shell pm uninstall com.microsoft.skype.teams.ipphone<br>
                        adb uninstall com.microsoft.teams.ipphone.admin.agent<br><i>
                        note:1.if u are connect more devices use -s after adb typed eg:adb -s <ip></i>""",
                        "unistall teams":"<b> first connect to ADB to run !! </b><br>  adb shell pm uninstall com.microsoft.skype.teams.ipphone<br><i>note:1.if u are connect more devices use -s after adb typed eg:adb -s <ip></i>",
                        "unistall cp":"<b>first connect to ADB to run !!</b><br>  adb shell pm uninstall com.microsoft.windowsintune.companyportal <br> <i>note:1.if u are connect more devices use -s after adb typed eg:adb -s <ip> </i> " ,
                        "unistall admin adgent":"<b>first connect to ADB to run !! </b><br>  adb uninstall com.microsoft.teams.ipphone.admin.agent <br> <i>note:1.if u are connect more devices use -s after adb typed eg:adb -s <ip></i>"

                }

    def disconnect(self):
                    self.dis=["how to disconnect adb", "adb disconnect","disconnect adb"]
                    self.responses={
                    "how to disconnect adb":"<b> first connect to ADB to run!!  </b> <br> <b>Open CMD  </b><br>use this command  <br> adb disconnect",
                    "adb disconnect":"<b> first connect to ADB to run!!  </b> <br> <b>Open CMD  </b><br>use this command  <br> adb disconnect",
                    "disconnect adb":"<b> first connect to ADB to run!!  </b> <br> <b>Open CMD  </b><br>use this command  <br> adb disconnect"
                }
    def install(self):
                self.ins=["teams install","cp install","cp oldversion install","teams oldversion install"]
                self.responses={
                    "teams install":"<b> first connect to ADB to run!!  </b> <br> <b>Open CMD  </b><br> use this command  <br> <b> adb install <file path in your PC> </b><br><i> note:1.remove <file path in your PC> and give file path in your PC <br> 2.if u are connect more devices use -s after adb typed eg:adb -s <ip></i>",
                    "cp install":"<b> first connect to ADB to run!!  </b> <br> <b>Open CMD  </b><br> use this command  <br> <b> adb install <file path in your PC> </b><br> <i> note:1.remove <file path in your PC> and give file path in your PC <br> 2.if u are connect more devices use -s after adb typed eg:adb -s <ip></i>",
                    "cp oldversion install":"<b> first connect to ADB to run!!  </b> <br> <b>Open CMD  </b><br> use this command  <br> <b> adb install  -d <file path in your PC> </b><br><i> note:1.remove <file path in your PC> and give file path in your PC <br> 2.if u are connect more devices use -s after adb typed eg:adb -s <ip></i>",
                    "teams oldversion install":"<b> first connect to ADB to run!!  </b> <br> <b>Open CMD  </b><br> use this command  <br> <b> adb install  -d <file path in your PC> </b><br><i> note:1.remove <file path in your PC> and give file path in your PC <br> 2.if u are connect more devices use -s after adb typed eg:adb -s <ip></i>"
                }
    def logcat(self):
                self.Logs=["run logs","logcat"]
                self.responses={
                    "run logs":"<b> first connect to ADB to run!!  </b> <br> <b>Open CMD </b><br> use this command  <br> adb logcat > filename.txt <br> <i>note:1.remove <filename> and give any name  <br> 2.if u are connect more devices use -s after adb typed eg:adb -s <ip> <br> 3. it will automatically saved in the path </i>",
                    "logcat":"<b> first connect to ADB to run!!  </b> <br> <b> Open CMD  </b><br> use this command  <br> adb logcat > filename.txt <br> <i>note:1.remove <filename> and give any name  <br> 2.if u are connect more devices use -s after adb typed eg:adb -s <ip> <br> 3. it will automatically saved in the path </i>"
                    }
    def Reboot_devices(self):
                self.RE_dev=["reboot command","reboot","devices list","device list"]
                self.responses={
                    "reboot command":"<b> first connect to ADB to run!!  </b> <br> <b>Open CMD   use this command  </b><br> adb reboot </b><br<i> note:1.if u are connect more devices use -s after adb typed eg:adb -s <ip>  </i>",
                    "reboot":"<b> first connect to ADB to run!!  </b> <br> <b>Open CMD  </b><br> use this command  </b><br> adb reboot </b><br> <i>note:1.if u are connect more devices use -s after adb typed eg:adb -s <ip> </i> ",
                    "devices list":"<b> first connect to ADB to run!!  </b> <br> <b>Open CMD  </b><br> use this command  </b><br> <b>adb  devices</b><br>",
                    "device list":"<b> first connect to ADB to run!!  </b> <br> <b>Open CMD  </b><br> use this command  </b><br> <b>adb  devices</b><br>",
                    
                    }  

    def Bugreport(self):
                self.bug=["bugreport command","bugreport"]
                self.responses={
                    "bugreport command":"<b> first connect to ADB to run!!  </b> <br> <b>Open CMD  </b><br> use this command  </b><br>  adb bugreport <br>  <i>note:1.if u are connect more devices use -s after adb typed eg:adb -s <ip> </i> ",
                    "bugreport":"<b> first connect to ADB to run!!  </b> <br> <b>Open CMD  </b><br> use this command  </b><br> adb bugreport<br> <i>note:1.if u are connect more devices use -s after adb typed eg:adb -s <ip>  </i>"
                    
                    } 
    def Ipconfig(self):
                self.ip=["sysinfo","system details","device info"]
                self.responses={
                    "sysinfo":"<b>Open CMD  </b><br> use this command <br>type : ipconfig  ",
                    "system details":"<b>Open CMD  </b><br> use this command <br>type : ipconfig   ",
                    "device info":"<b>Open CMD  </b><br> use this command <br>type : ipconfig  "
                    
                    } 
    def devicecap(self):
                self.dev=["device capabilities"]
                self.responses={
                        "device capabilities":"""<b>first connect to ADB to run !! </b><br>
                         then run this command <b>  adb shell settings get secure teams_device_capabilities</b>"""
                    } 
    def slimcore(self):
                self.slim=["slim core logs","store cache logs"]
                self.responses={
                        "slim core logs":"""<i>  call related issues take Slim core logs </i><b>first connect to ADB to run !! </b><br>
                         then run this command <b> adb.exe pull /sdcard/Android/data/com.microsoft.skype.teams.ipphone/cache</b>""",
                         "store cache logs":"""<i>  call related issues take Slim core logs </i><b>first connect to ADB to run !! </b><br>
                         then run this command <b> adb.exe pull /sdcard/Android/data/com.microsoft.skype.teams.ipphone/cache</b>"""
                    } 
    def screenshot(self):
            self.scr=["screen capture","adb using screen capture" ,"screen shot adb","screen capture using adb"]
            self.responses={
                        "screen capture":"""<b> this command is used in adb <br> first connect to ADB to run !! </b><br>
                         then run this command <b> adb exec-out screencap -p > screen.png</b>""",
                         "adb using screen capture":"""<b> first connect to ADB to run !! </b><br>
                         then run this command <b> adb exec-out screencap -p > screen.png</b>""",
                         "screen shot adb":"""<b> first connect to ADB to run !! </b><br>
                         then run this command <b> adb exec-out screencap -p > screen.png</b>""",
                         "screen capture using adb":"""<b> first connect to ADB to run !! </b><br>
                         then run this command <b> adb exec-out screencap -p > screen.png</b>"""
                         
            }
    def screenrecord(self):
            self.record=["screen recording","adb using screen recording" ,"screen recording adb","screen recording using adb"]
            self.responses={
                        "screen recording":"""<b> this command is used in adb <br> first connect to ADB to run !! </b><br>
                         then run this command <b> adb shell screenrecord /sdcard/video.mp4</b>""",
                         "adb using screen recording":"""<b> first connect to ADB to run !! </b><br>
                         then run this command <b> adb shell screenrecord /sdcard/video.mp4 </b>""",
                         "screen recording adb":"""<b> first connect to ADB to run !! </b><br>
                         then run this command <b> adb shell screenrecord /sdcard/video.mp4 </b>""",
                         "screen recording using adb":"""<b> first connect to ADB to run !! </b><br>
                         then run this command <b> adb shell screenrecord /sdcard/video.mp4 </b>"""
                         }
    def cplogs(self):
                self.cp=["cp logs"]
                self.responses={
                        "cp logs":"""<i>CP logs: When any sign in issue occure take CP logs </i> <br> <b>first connect to ADB to run !! </b><br>
                          <b> adb shell am broadcast -a com.microsoft.windowsintune.companyportal.intent.action.IPPHONE_UPLOAD_LOGS --es SessionID "GUID CODE(EG:3a3a5de7-91a8-4a74-bdfe-0a0b5c3d98d1)" -n com.microsoft.windowsintune.companyportal/.omadm.IPPhoneReceiver
</b> <br><i> for guid code then vist this website and copy that code and paste in the guid code</i> <br> <b> website::https://www.guidgenerator.com/online-guid-generator.aspx"""
                        
                    }         
    def version(self):
                self.ver=["android version","firmware version","os version","version code","device encryption"]
                self.responses={
                        "android version":"""<b>first connect to ADB to run !! </b><br>
                         then run this command <b> adb shell getprop ro.build.version.release</b>""",
                        "firmware version":"""<b>first connect to ADB to run !! </b><br>
                         then run this command <b>adb shell getprop build.firmware.version</b>""",
                        "os version":"""<b>first connect to ADB to run !! </b><br>
                         then run this command <b>adb shell getprop ro.build.version.release</b>""",
                         "version code":"""<b>first connect to ADB to run !! </b><br>
                         then run this command <b>adb shell dumpsys package com.microsoft.teams.ipphone.admin.agent | findstr versionCode</b>""",
                         "device encryption":"""<b>first connect to ADB to run !! </b><br>
                         then run this command <b>adb shell getprop ro.crypto.state</b>"""    
                    }     
    def size_density(self):
                self.si_de=["adb command for size","to check 1080","adb command for density","to check dpi density"]
                self.responses={
                        "adb command for size":"""<b>first connect to ADB to run !! </b><br>
                         then run this command <b>adb shell wm size</b>""",
                        "to check 1080":"""<b>first connect to ADB to run !! </b><br>
                         then run this command <b>adb shell wm size</b>""",
                        "adb command for density":"""<b>first connect to ADB to run !! </b><br>
                         then run this command <b>adb shell wm density</b>""",
                         "to check dpi density":"""<b>first connect to ADB to run !! </b><br>
                         then run this command <b>adb shell wm density</b>"""    
                    }   
    def XL_meet(self):
            self.xl=["how to create xl meet","xl meet"]
            self.responses={
                    "how to create xl meet":"""<i> Pre-requisite: <br>
                    1) Meeting Link from meeting created by R0(V-) MS account.<br>
                    2) botgen6.zip - Attached</i><br>
                    Steps:
                    1) Use this botgen6.zip (Attached) for adding bots to meeting, bots will be there for 15 minutes after 
                    adding only<br>
                    2) Please extract this zip file and then use command prompt and navigate to the directory where this is 
                    saved.<br>
                    3) Once there, use this command to add bots<br>
                    4) <b>  .\\botgen.exe --meetingUrl <meeting url> --videoBotCount <bot count></b><br>
                    5) Replace <meeting url> with the meeting link, and <bot count> with number of bots needed
                    """,
                    "xl meet":"""<i> Pre-requisite: <br>
                    1) Meeting Link from meeting created by R0(V-) MS account.<br>
                    2) botgen6.zip - Attached</i><br>
                    Steps:
                    1) Use this botgen6.zip (Attached) for adding bots to meeting, bots will be there for 15 minutes after 
                    adding only<br>
                    2) Please extract this zip file and then use command prompt and navigate to the directory where this is 
                    saved.<br>
                    3) Once there, use this command to add bots<br>
                    4) <b>  .\\botgen.exe --meetingUrl <meeting url> --videoBotCount <bot count></b><br>
                    5) Replace <meeting url> with the meeting link, and <bot count> with number of bots needed
                    """
            }
    def cisco(self):
            self.cis_en=["adb cisco enable","cisco enable","cisco adb enable"]
            self.responses={"adb cisco enable":"""1. Open the CMD enter the command <br><b>adb keygen C:\\Users\\v-naveenka\\adbkey   </b><i> in this (\\v-naveenka change and keep your folder name) <br>
                            2.<b>type C:\\Users\\v-naveenka\\adbkey.pub </b> <i> after entered you can osberve the key copy that data </i> <br>3.open the <b>WEB UI of cisco device</b> and paste the data with the command<br>4. <i> after given admin user id and password go to developer API </i> <br><b>xCommand SystemUnit Extension Adb Enable Key:  “ paste the data u copy  ”  </b> click execute  <br> 5.<b> then connect the device adb connect ip-address-of-device </b> <br>  <i>Note:1 .Some times u  get failed to authenticate then use the command <b>adb kill-server and adb start-server</b> and try u can get</i>""",
                           "cisco enable":"""1. Open the CMD enter the command <br><b>adb keygen C:\\Users\\v-naveenka\\adbkey   </b><i> in this (\\v-naveenka change and keep your folder name) <br>
                            2.<b>type C:\\Users\\v-naveenka\\adbkey.pub </b> <i> after entered you can osberve the key copy that data </i> <br>3.open the <b>WEB UI of cisco device</b> and paste the data with the command<br>4. <i> after given admin user id and password go to developer API </i> <br><b>xCommand SystemUnit Extension Adb Enable Key:  “ paste the data u copy  ”  </b> click execute  <br> 5.<b> then connect the device adb connect ip-address-of-device </b> <br>  <i>Note:1 .Some times u  get failed to authenticate then use the command <b>adb kill-server and adb start-server</b> and try u can get</i>""",
                            "cisco adb enable":"""1. Open the CMD enter the command <br><b>adb keygen C:\\Users\\v-naveenka\\adbkey   </b><i> in this (\\v-naveenka change and keep your folder name) <br>
                            2.<b>type C:\\Users\\v-naveenka\\adbkey.pub </b> <i> after entered you can osberve the key copy that data </i> <br>3.open the <b>WEB UI of cisco device</b> and paste the data with the command<br>4. <i> after given admin user id and password go to developer API </i> <br><b>xCommand SystemUnit Extension Adb Enable Key:  “ paste the data u copy  ”  </b> click execute  <br> 5.<b> then connect the device adb connect ip-address-of-device </b> <br>  <i>Note:1 .Some times u  get failed to authenticate then use the command <b>adb kill-server and adb start-server</b> and try u can get</i>"""

                            }
    
    
    
    def pull_push(self):
            self.pu_pl=["adb pull","adb push"]
            self.responses={"adb pull":"""<b>first connect to ADB to run !! </b><br>
                         then run this command <b> 
                         adb pull storage/emulated/0/Android/data/com.microsoft.teams.ipphone.admin.agent/files/ConfigDirectory/Config.json</b>""",
                        "adb push":"""<b>first connect to ADB to run !! </b><br>
                         then run this command <b>adb push Config.json /storage/emulated/0/Android/data/com.microsoft.teams.ipphone.admin.agent/files/ConfigDirectory/Config.json</b>"""}  
            



    #---------------- DM commands---------
    def tac(self):
            self.Tac=["tac","open tac"]
            self.responses={"tac":""" <b>Types of Microsoft teams admin centre</b> <br> 
                1.Pre-production Environment (PPE) /Develop <br>
                2.Production Environment  <br> <b> How to bring Teams android device into PPE</b><br><b> 
                Adb pull: </b>

                1.adb pull storage/emulated/0/Android/data/com.microsoft.teams.ipphone.admin.agent/files/ConfigDirectory/Config.json <br>
                2. Start -> check the file that managed in command prompt <br>
                <br>
                Open the config file By selecting text document  -> a edit that file with respect to the need ( Production , Develop ) 
                <br> PPE Link: -> Develop <br>
                <i>webiste:</i><a href= https://admin-int.teams.microsoft.net  style="color: darkblue ;">https://admin-int.teams.microsoft.net</a> 
                <br><b>email:teamsdeviceadministrator@3PIP.onmicrosoft.com<br>
                password:Ipphones@01</b>
                <br> How to bring Teams android device into production  <br> 1. By default all partner  Devices will be in production  
                            Prod Link: -> Production <i>webiste:</i><a href= https://admin.teams.microsoft.com  style="color: darkblue ;">https://admin.teams.microsoft.com </a> <br><b> email: teamsdeviceadministrator@3PIP.onmicrosoft.com <br>
                password:Ipphones@01 <br>
                """  ,
                "open tac":""" <b>Types of Microsoft teams admin centre</b> <br> 
                1.Pre-production Environment (PPE) /Develop <br>
                2.Production Environment  <br> <b> How to bring Teams android device into PPE</b><br><b> 
                Adb pull: </b>

                1.adb pull storage/emulated/0/Android/data/com.microsoft.teams.ipphone.admin.agent/files/ConfigDirectory/Config.json <br>
                2. Start -> check the file that managed in command prompt <br>
                <br>
                Open the config file By selecting text document  -> a edit that file with respect to the need ( Production , Develop ) 
                <br> PPE Link: -> Develop <br>
                <i>webiste:</i><a href= https://admin-int.teams.microsoft.net  style="color: darkblue ;">https://admin-int.teams.microsoft.net</a> 
                <br><b>email:teamsdeviceadministrator@3PIP.onmicrosoft.com<br>
                password:Ipphones@01</b>
                <br> How to bring Teams android device into production  <br> 1. By default all partner  Devices will be in production  
                            Prod Link: -> Production <i>webiste:</i><a href= https://admin.teams.microsoft.com  style="color: darkblue ;">https://admin.teams.microsoft.com </a> <br><b> email: teamsdeviceadministrator@3PIP.onmicrosoft.com <br>
                password:Ipphones@01 <br>
                """  
 
            }
    def provision(self):
                self.pro=["how to do provision in tac","tac provision"]
                self.responses={
                            "how to do provision in tac":""" 1.Select cloud in DUT(Device under test) by navigating to settings >cloud <br>
                            <i> <i>forGCCH:</i><a href= https://admin.gov.teams.microsoft.us/>https://admin.gov.teams.microsoft.us/</a><br>
                            email:v-naveenka@quovadimus.ms   Password: Phones@01<br>
                            email:v-keziasimon@quovadimus.ms   Password: K@zi123<br>
                            <i>DOD :</i><a href=https://Dod.teams.microsoft.us>https://Dod.teams.microsoft.us</a><br>
                            <i>DOD :</i><a href=https://admin.dod.teams.microsoft.us/>https://admin.dod.teams.microsoft.us/</a><br>
                            email:v-keziasimon@nexuszone.redacted.zone	      Password:RA>R-Xv#%k%?cTJ:{G%9 <br>
                            GCC ACCOUNT: (DUT should be Prod env.) for Govt clouds logs also<br>
                            <i>Admin credentials for GCC::</i><a href= https://admin.teams.microsoft.com>https://admin.teams.microsoft.com</a><br>
                            email:administrator@tdgcc.onmicrosoft.com    password:P@ssword1
                            <br>
                            Public Account: <i>webiste:</i><a href= https://admin-int.teams.microsoft.net  style="color: darkblue ;" > https://admin-int.teams.microsoft.net </a>(PPE)<br>
                            <i>webiste:</i><a href= https://admin.teams.microsoft.com style="color: darkblue ;" >https://admin.teams.microsoft.com </a>(Production)</i><br>
                        2.Open the Microsoft Teams admin Centre in your PC by using Respective URL according to the which environment your Device is configured .<br>
                        3.Enter PPE or production URL in your PC 
                                   <i>webiste:</i><a href= https://admin-int.teams.microsoft.net  style="color: darkblue ;" > https://admin-int.teams.microsoft.net </a>(PPE)<br>
                                    <i>webiste:</i><a href= https://admin.teams.microsoft.com style="color: darkblue ;" >https://admin.teams.microsoft.com </a>(Production)
                                    <br>4.Enter admin user name and password <b> email: teamsdeviceadministrator@3PIP.onmicrosoft.com  password:Ipphones@01 </b><br>
                                    5.After admin sign in is successful Microsoft teams admin centre is launched<br>
                                    6.Select My device in Microsoft admin teams centre<br>
                                    7.Select which model devices are need to be provision  under Teams devices option <br>
                                    8.select any category <i>(eg :phones) </i>
                                     <br> 9.Once phones is selected All the phones category devices are displayed  <br>
                                     10.click on “Action” which is displayed right corner <br>
                                     11.Click on provision devices under Action option. <br>
                                     12.Click on “Add “which is Highlighted blue in colour <br>
                                     13. IT admin needs to upload the MAC IDs of the devices being provisioned and Can be achieved using manually or uploading .xlsx format <br>
                                     14.Enter Device MAC id and Location  (Navigate to settings >Device settings>About in DUT) and click on save <br>
                                     15.After clicking on save “waiting Activation “list is displayed  under provision devices page in TAC  .<br>
                                     16. Select Device which need to be provisioned in the list <br>
                                     17.Click on Generate verification code >Code is generated <br>
                                     18. Navigate to settings >Provision device in DUT<br>
                                     19.Enter the verification code in DUT as show below , which is generated in TAC for particular device and click on next. <br>
                                     20.After clicking on next button popup should be shown as” Device is provisioned successfully” (if you provisioned the Device for first time) and if the Device is already provisioned a popup as to be shown as below<br>
                                     21.Now ,Go to TAC search for provisioned device by entering device name ,model, Ip address, Mac id, serial number  <br>
                                     22.open the selected device page in TAC <br>
                                     23.Click on sign in which is highlighted blue in colour  <br>
                                     24.After clicking the sign in link” sign in as user”  popup is displayed <br>
                                     25.Wait for DCF code to generate from admin . <br>
                                    26.Paralelley in DUT administrator is signing into the device popup<br>
                                    27.DCF code is generated with URL link  <br>
                                    28.Copy the code and click URL shown <br>
                                    29.Enter code page is displayed  and click on Next  <br>
                                    30.Enter valid user name and password >click on sign in <br>
                                    31.Device is signed in successfully in DUT<br>
                                    32.In TAC is showing Non -urgent and showing the user signed in<br>
                                    <i>Note  :For Accounts credentials contact Naveen and Kezia </i>""",
                "tac provision":""" 1.Select cloud in DUT(Device under test) by navigating to settings >cloud <br>
                        <i> <i>forGCCH:</i><a href= https://admin.gov.teams.microsoft.us/>https://admin.gov.teams.microsoft.us/</a><br>
                email:v-naveenka@quovadimus.ms   Password: Phones@01<br>
                email:v-keziasimon@quovadimus.ms   Password: K@zi123<br>
                

                <i>DOD :</i><a href=https://Dod.teams.microsoft.us>https://Dod.teams.microsoft.us</a><br>
                <i>DOD :</i><a href=https://admin.dod.teams.microsoft.us/>https://admin.dod.teams.microsoft.us/</a><br>
                
                email:v-keziasimon@nexuszone.redacted.zone	      Password:RA>R-Xv#%k%?cTJ:{G%9 <br>
                
                
                GCC ACCOUNT: (DUT should be Prod env.) for Govt clouds logs also<br>
                <i>Admin credentials for GCC::</i><a href= https://admin.teams.microsoft.com>https://admin.teams.microsoft.com</a><br>
                email:administrator@tdgcc.onmicrosoft.com    password:P@ssword1
                <br>
                Public Account: <i>webiste:</i><a href= https://admin-int.teams.microsoft.net  style="color: darkblue ;" > https://admin-int.teams.microsoft.net </a>(PPE)<br>
                                                    <i>webiste:</i><a href= https://admin.teams.microsoft.com style="color: darkblue ;" >https://admin.teams.microsoft.com </a>(Production)</i><br>
                        2.Open the Microsoft Teams admin Centre in your PC by using Respective URL according to the which environment your Device is configured .<br>
                        3.Enter PPE or production URL in your PC 
                                   <i>webiste:</i><a href= https://admin-int.teams.microsoft.net  style="color: darkblue ;" > https://admin-int.teams.microsoft.net </a>(PPE)<br>
                                    <i>webiste:</i><a href= https://admin.teams.microsoft.com style="color: darkblue ;" >https://admin.teams.microsoft.com </a>(Production)
                                    <br>4.Enter admin user name and password <b> email: teamsdeviceadministrator@3PIP.onmicrosoft.com  password:Ipphones@01 </b><br>
                                    5.After admin sign in is successful Microsoft teams admin centre is launched<br>
                                    6.Select My device in Microsoft admin teams centre<br>
                                    7.Select which model devices are need to be provision  under Teams devices option <br>
                                    8.select any category <i>(eg :phones) </i>
                                     <br> 9.Once phones is selected All the phones category devices are displayed  <br>
                                     10.click on “Action” which is displayed right corner <br>
                                     11.Click on provision devices under Action option. <br>
                                     12.Click on “Add “which is Highlighted blue in colour <br>
                                     13. IT admin needs to upload the MAC IDs of the devices being provisioned and Can be achieved using manually or uploading .xlsx format <br>
                                     14.Enter Device MAC id and Location  (Navigate to settings >Device settings>About in DUT) and click on save <br>
                                     15.After clicking on save “waiting Activation “list is displayed  under provision devices page in TAC  .<br>
                                     16. Select Device which need to be provisioned in the list <br>
                                     17.Click on Generate verification code >Code is generated <br>
                                     18. Navigate to settings >Provision device in DUT<br>
                                     19.Enter the verification code in DUT as show below , which is generated in TAC for particular device and click on next. <br>
                                     20.After clicking on next button popup should be shown as” Device is provisioned successfully” (if you provisioned the Device for first time) and if the Device is already provisioned a popup as to be shown as below<br>
                                     21.Now ,Go to TAC search for provisioned device by entering device name ,model, Ip address, Mac id, serial number  <br>
                                     22.open the selected device page in TAC <br>
                                     23.Click on sign in which is highlighted blue in colour  <br>
                                     24.After clicking the sign in link” sign in as user”  popup is displayed <br>
                                     25.Wait for DCF code to generate from admin . <br>
                                    26.Paralelley in DUT administrator is signing into the device popup<br>
                                    27.DCF code is generated with URL link  <br>
                                    28.Copy the code and click URL shown <br>
                                    29.Enter code page is displayed  and click on Next  <br>
                                    30.Enter valid user name and password >click on sign in <br>
                                    31.Device is signed in successfully in DUT<br>
                                    32.In TAC is showing Non -urgent and showing the user signed in<br>
                                    <i>Note  :For Accounts credentials contact Naveen and Kezia </i>"""
                                    }
    def fingerprint(self):
                self.fing=["fingerprint command","fingerprint","adb command for fingerprint"]
                self.responses={
                        "fingerprint command":"""<b>first connect to ADB to run !! </b><br>
                         then run this command <b> 
                         adb shell "getprop | grep -iE 'ro.system.build.fingerprint|securityfused|logi.fwupd.ver|manifest-current-ver'"</b>""",
                          "fingerprint":"""<b>first connect to ADB to run !! </b><br>
                         then run this command <b> 
                         adb shell "getprop | grep -iE 'ro.system.build.fingerprint|securityfused|logi.fwupd.ver|manifest-current-ver'"</b>""",
                          "adb command for fingerprint":"""<b>first connect to ADB to run !! </b><br>
                         then run this command <b> 
                         adb shell "getprop | grep -iE 'ro.system.build.fingerprint|securityfused|logi.fwupd.ver|manifest-current-ver'"</b>"""
                }
            

    
    def process_input(self, user_input):
                # Remove extra spaces and convert to lowercase
                return " ".join(user_input.split()).lower()
    def generate_response(self, user_input):   
                user_input = self.process_input(user_input)

                
                if user_input in self.greetings:
                        return self.responses.get(user_input,"hii team ask me anything iam ready") 
                
                elif user_input in self.goodbyes:
                    return self.responses.get(user_input, "Goodbye! Have a great day!")
                    
                chatbot.clear()
            
                if user_input in self.c:
                    return self.responses.get(user_input)
                elif user_input in self.u:
                    return self.responses.get(user_input)
                
                chatbot.connect()
                if user_input in self.con:
                    return self.responses.get(user_input)
                chatbot.disconnect()
                if user_input in self.dis:
                    return self.responses.get(user_input)
                chatbot.install()
                if user_input in self.ins:
                    return self.responses.get(user_input)
                chatbot.logcat()
                if user_input in self.Logs:
                    return self.responses.get(user_input)
                chatbot.Reboot_devices()
                if user_input in self.RE_dev:
                    return self.responses.get(user_input)
                chatbot.Bugreport()
                if user_input in self.bug:
                    return self.responses.get(user_input)
                chatbot.Ipconfig()
                if user_input in self.ip:
                    return self.responses.get(user_input)
                chatbot.size_density()
                if user_input in self.si_de:
                    return self.responses.get(user_input)
                chatbot.devicecap()
                if user_input in self.dev:
                    return self.responses.get(user_input)
                chatbot.screenshot()
                if user_input in self.scr:
                        return self.responses.get(user_input)
                chatbot.screenrecord()
                if user_input in self.record:
                        return self.responses.get(user_input)
                chatbot.version()
                if user_input in self.ver:
                        return self.responses.get(user_input)
                chatbot.cplogs()
                if user_input in self.cp:
                        return self.responses.get(user_input)
                chatbot.slimcore()
                if user_input in self.slim:
                        return self.responses.get(user_input)
                chatbot.XL_meet()
                if user_input in self.xl:
                        return self.responses.get(user_input)
                chatbot.pull_push()
                if user_input in self.pu_pl:
                        return self.responses.get(user_input)
                chatbot.cisco()
                if user_input in self.cis_en:
                        return self.responses.get(user_input)
                chatbot.tac()
                if user_input in self.Tac:
                        return self.responses.get(user_input)
                chatbot.provision()
                if user_input in self.pro:
                        return self.responses.get(user_input)
                chatbot.fingerprint()
                if user_input in self.fing:
                        return self.responses.get(user_input)

                else:
                    return "Sorry, I didn't understand that please type correct . How can I help you? "
                     
 
            
            
        
    # Example usage
chatbot =Norden()


    



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.form['user_message']
    bot_response = chatbot.generate_response(user_message)
    return jsonify({'bot_response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
