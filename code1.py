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
                    "how to connect adb":"Open CMD  \n use this command  \n adb connect <ip address of the device> \n note: remove <ip address of the device> and give IP",
                    "adb connect":"Open CMD  \n use this command  \n adb connect <ip address of the device>\n note: remove <ip address of the device> and give IP",
                    "connect the devices":"Open CMD  \n use this command  \n adb connect <ip address of the device>\n note: remove <ip address of the device> and give IP",
                    "connect adb":"Open CMD  \n use this command  \n adb connect <ip address of the device>\n note: remove <ip address of the device> and give IP"
                }

    def clear(self):
                self.c=["clear commands","clear cache commands","clear teams cache"]
                self.u=["unistall commands list","unistall teams commands ","unistall teams","unistall cp","unistall admin adgent"]
                self.responses={ 
                    "clear commands":"""  first connect to ADB to run!!  To clear cache for device
                adb shell pm clear com.microsoft.skype.teams.ipphone
                    adb shell pm clear com.microsoft.windowsintune.companyportal
                    adb shell pm clear com.microsoft.teams.ipphone.admin.agent
                    note:1.if u are connect more devices use -s after adb typed eg:adb -s <ip>""",
                    "clear cache commands":"""first connect to ADB to run!!  To clear cache for device
                adb shell pm clear com.microsoft.skype.teams.ipphone
                    adb shell pm clear com.microsoft.windowsintune.companyportal
                    adb shell pm clear com.microsoft.teams.ipphone.admin.agent
                    note:1.if u are connect more devices use -s after adb typed eg:adb -s <ip>""",
                    "clear teams cache":"""   first connect to ADB to run!! To clear cache for device
                adb shell pm clear com.microsoft.skype.teams.ipphone
                    adb shell pm clear com.microsoft.windowsintune.companyportal
                    adb shell pm clear com.microsoft.teams.ipphone.admin.agent
                    note:1.if u are connect more devices use -s after adb typed eg:adb -s <ip>""",
                    "unistall commands list":""" first connect to ADB to run !!
                        adb shell pm uninstall com.microsoft.windowsintune.companyportal
                        adb shell pm uninstall com.microsoft.skype.teams.ipphone
                        adb uninstall com.microsoft.teams.ipphone.admin.agent
                        note:1.if u are connect more devices use -s after adb typed eg:adb -s <ip>""",
                    "unistall teams commands ":""" first connect to ADB to run !!
                        adb shell pm uninstall com.microsoft.windowsintune.companyportal
                        adb shell pm uninstall com.microsoft.skype.teams.ipphone
                        adb uninstall com.microsoft.teams.ipphone.admin.agent
                        note:1.if u are connect more devices use -s after adb typed eg:adb -s <ip>""",
                        "unistall teams":"first connect to ADB to run !!   adb shell pm uninstall com.microsoft.skype.teams.ipphone note:1.if u are connect more devices use -s after adb typed eg:adb -s <ip>",
                        "unistall cp":"first connect to ADB to run !!  adb shell pm uninstall com.microsoft.windowsintune.companyportal note:1.if u are connect more devices use -s after adb typed eg:adb -s <ip>  " ,
                        "unistall admin adgent":"first connect to ADB to run !!   adb uninstall com.microsoft.teams.ipphone.admin.agent note:1.if u are connect more devices use -s after adb typed eg:adb -s <ip>"

                }

    def disconnect(self):
                    self.dis=["how to disconnect adb", "adb disconnect","disconnect adb"]
                    self.responses={
                    "how to disconnect adb":"Open CMD  \n use this command  \n adb disconnect",
                    "adb disconnect":"Open CMD  \n use this command  \n adb disconnect",
                    "disconnect adb":"Open CMD  \n use this command  \n adb disconnect"
                }
    def install(self):
                self.ins=["teams install","cp install","cp oldversion install","teams oldversion install"]
                self.responses={
                    "teams install":"Open CMD  \n use this command  \n adb install <file path in your PC> \n note:1.remove <file path in your PC> and give file path in your PC \n 2.if u are connect more devices use -s after adb typed eg:adb -s <ip>",
                    "cp install":"Open CMD  \n use this command  \n adb install <file path in your PC> \n note:1.remove <file path in your PC> and give file path in your PC \n 2.if u are connect more devices use -s after adb typed eg:adb -s <ip>",
                    "cp oldversion install":"Open CMD  \n use this command  \n adb install -d <file path in your PC> \n note:1.remove <file path in your PC> and give file path in your PC \n 2.if u are connect more devices use -s after adb typed eg:adb -s <ip>",
                    "teams oldversion install":"Open CMD  \n use this command  \n adb install -d <file path in your PC> \n note:1.remove <file path in your PC> and give file path in your PC \n 2.if u are connect more devices use -s after adb typed eg:adb -s <ip>"
                }
    def logcat(self):
                self.Logs=["run logs","logcat"]
                self.responses={
                    "run logs":"Open CMD  \n use this command  \n adb logcat > filename.txt \n note:1.remove <filename> and give any name  \n 2.if u are connect more devices use -s after adb typed eg:adb -s <ip> \n 3. it will automatically saved in the path ",
                    "logcat":" Open CMD  \n use this command  \n adb logcat > filename.txt \n note:1.remove <filename> and give any name  \n 2.if u are connect more devices use -s after adb typed eg:adb -s <ip> \n 3. it will automatically saved in the path "
                    }
    def Reboot(self):
                self.RE=["reboot command","reboot"]
                self.responses={
                    "reboot command":"Open CMD  \n use this command  \n adb reboot \n note:1.if u are connect more devices use -s after adb typed eg:adb -s <ip>  ",
                    "reboot":"Open CMD  \n use this command  \n adb reboot \n note:1.if u are connect more devices use -s after adb typed eg:adb -s <ip>  "
                    }  

    def Bugreport(self):
                self.bug=["bugreport command","bugreport"]
                self.responses={
                    "bugreport command":"Open CMD  \n use this command  \n adb bugreport \n note:1.if u are connect more devices use -s after adb typed eg:adb -s <ip>  ",
                    "bugreport":"Open CMD  \n use this command  \n adb bugreport \n note:1.if u are connect more devices use -s after adb typed eg:adb -s <ip>  "
                    
                    } 
    def Ipconfig(self):
                self.ip=["sysinfo","system details","device info"]
                self.responses={
                    "sysinfo":"Open CMD  \n use this command  \n type : ipconfig  ",
                    "system details":"Open CMD  \n use this command  \n type : ipconfig  ",
                    "device info":"Open CMD  \n use this command  \n type : ipconfig  "
                    
                    } 


    def process_input(self, user_input):
                # Remove extra spaces and convert to lowercase
                return " ".join(user_input.split()).lower()
    def generate_response(self, user_input):   
                user_input = self.process_input(user_input)

                
                if user_input in self.greetings:
                        return self.responses.get(user_input,"hi my team") 
                
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
                chatbot.Reboot()
                if user_input in self.RE:
                    return self.responses.get(user_input)
                chatbot.Bugreport()
                if user_input in self.bug:
                    return self.responses.get(user_input)
                chatbot.Ipconfig()
                if user_input in self.ip:
                    return self.responses.get(user_input)
                
                else:
                    return "Sorry, I didn't understand that please type correct . How can I help you? "
                     
 
            
            
        
    # Example usage
chatbot =Norden()
print("Welcome! Type 'bye' to exit.")
while True:
            user_input = input("You: ")
            response = chatbot.generate_response(user_input)
            print("Bot:", response)
            if user_input.lower() in chatbot.goodbyes:
                break

    