# this code has a lot of incomplete functions this will be finished soon
# currently the Xbox auth works and thats about it

import customtkinter 
import requests
import json
from PIL import Image
import os
from tkinter import messagebox
import time

#saves xbox token so you can use it later and not have to keep intputting it
XBL_TOKEN = ""

# for party stuff (coming soon)
xuidURL = "https://profile.xboxlive.com/users/me/id"
partyURL = "https://sessiondirectory.xboxlive.com/serviceconfigs/7492BACA-C1B4-440D-A391-B7EF364A8D40/sessiontemplates/chat/sessions/3411d1e1-24f1-44d3-b830-8616a458629c"
inviteURL = "https://sessiondirectory.xboxlive.com/handles"

#xbox title ids (for spoofing)
def xbox_title_ids():
    list = requests.get("https://pastebin.com/raw/5U2zYnFq")
    print(list)

#code for xbox party tools

def spoof_games():
    app = customtkinter.CTk()
    app.geometry("300x300")
    app.title("Game Spoofer")
    combobox = customtkinter.CTkComboBox(master=app,
                                        values=["option 1", "option 2"])
    combobox.pack(padx=20, pady=10)
    combobox.set("")  # set initial value

    app.mainloop()

class InviteSpam(customtkinter.CTk):
    def __init__(self):
        app = customtkinter.CTk()
        app.geometry("300x300")
        app.title("Message Spam")

        self.XUID = customtkinter.CTkEntry(app, placeholder_text="Target XUID Here...", width=300)
        self.XUID.pack(pady=10)

        self.message = customtkinter.CTkEntry(app, placeholder_text="Enter Message Here...", width=300)
        self.message.pack(pady=10)

        button_authorize = customtkinter.CTkButton(app, text="SPAM!!!", command=self.invite_spam, width=300)
        button_authorize.pack(pady=10)

        app.mainloop()

    def invite_spam(self):
        xuidURL = "https://profile.xboxlive.com/users/me/id"
        xuid = ""

        #body = "{\"type\":\"invite\",\"sessionRef\":{\"scid\":\"7492BACA-C1B4-440D-A391-B7EF364A8D40\",\"templateName\":\"chat\",\"name\":\"3411d1e1-24f1-44d3-b830-8616a458629c\"},\"invitedXuid\":\"" + Inviteboxtxt.Text + "\"}";
        setup = "{\"constants\":{\"custom\":{\"bumblelion\":true}},\"properties\":{\"system\":{\"joinRestriction\":\"followed\",\"readRestriction\":\"followed\"}},\"members\":{\"me_" + xuid + "\":{\"constants\":{\"custom\":{\"clientCapability\":\"8\"},\"system\":{\"xuid\":\"" + xuid + "\"}},\"properties\":{\"custom\":{\"isBroadcasting\":false,\"simpleConnectionState\":\"1\", \"deviceId\":\"73129482-568B-452C-BBD5-021E64A28FD3\"},\"system\":{\"ready\":true}}}}}" # this creats the party

        response = requests.post(setup, headers=setup, data=XBL_TOKEN)
        #response2 = requests.post(xbox_invite_api, headers=headers, json=data)

        if response.status_code == 200:
            print("Request successful")
            print(response.text)  # Print the response text (content from the server)
        else:
            print("Request failed with status code:", response.status_code)
            print(response.text)

class GTTOXUID(customtkinter.CTk):
    def __init__(self):
        app = customtkinter.CTk()
        app.geometry("300x300")
        app.title("XUID to GT")

        self.gamertag = customtkinter.CTkEntry(app, placeholder_text="Target Gamertag Here...", width=300)
        self.gamertag.pack(pady=10)

        self.output = customtkinter.CTkEntry(app, placeholder_text="Output Here...", width=300)
        self.output.pack(pady=10)

        button_authorize = customtkinter.CTkButton(app, text="Gamertag To XUID", command=self.gamertagtoxuid, width=300)
        button_authorize.pack(pady=10)

        app.mainloop()

    def gamertagtoxuid(self):
        url = f"https://profile.xboxlive.com/users/gt({self.gamertag})/profile/settings"
        
        headers = {
            "x-xbl-contract-version": "2",
            "Accept-Encoding": "gzip, deflate",
            "accept": "application/json",
            "accept-language": "en-GB",
            "Authorization": f"{XBL_TOKEN}",
            "Host": "profile.xboxlive.com",
            "Connection": "Keep-Alive"
        }
        
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            response_data = response.json()
            xuid = response_data['profileUsers'][0]['id']
            print("XUID:", xuid)  
        else:
            print(f"Request failed with status code: {response.status_code}")

def authorize_xbox_token():
    global XBL_TOKEN
    XBL_TOKEN = Token.get()
    xbox_auth_api = f"https://profile.xboxlive.com/users/me/profile/settings?settings=Gamertag,Gamerscore"

    headers = {
        'Connection': 'Keep-Alive',
        'Host': 'profile.xboxlive.com',
        'Authorization': f'{XBL_TOKEN}',
        'accept-language': 'en-GB',
        'accept': 'application/json',
        'Accept-Encoding': 'gzip, deflate',
        'x-xbl-contract-version': '2'
    }

    response = requests.get(xbox_auth_api, headers=headers)

    if response.status_code == 200:
        messagebox.showinfo("Xbox Token", "Xbox Token Successfully Authorized!")
        time.sleep(2)
        output.delete("0.0", "end") # deletes existing content  
        output.insert("0.0", "Xbox Token Successfully Authorized!") # outputs message
    else:
        messagebox.showerror("Xbox Token", "There is a problem with the Token provided!\n\nJoin the Discord for help: ")
        output.delete("0.0", "end") 
        output.insert("0.0", "There is a problem with the Token provided!") 

def check_token():
    output.delete("0.0", "end") 
    output.insert("0.0", f"{XBL_TOKEN}") 

#customtkinter GUI stuff below        
app = customtkinter.CTk()
app.geometry("600x800")
app.title("Robins Xbox Tool's | BETA | More Coming Soon...")

#auto dark appearance
customtkinter.set_appearance_mode("dark")

#so you cant resize the window
app.resizable(False, False)

image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets")

logo_image = Image.open(os.path.join(image_path, "logo.png"))
logo = customtkinter.CTkImage(dark_image=logo_image, size=(170, 200))  

image_label = customtkinter.CTkLabel(app, image=logo, text="")
image_label.pack(pady=10)

Token = customtkinter.CTkEntry(app, placeholder_text="XBL Token Here", width=300)
Token.pack(pady=10)

button_authorize = customtkinter.CTkButton(app, text="Authorize XBL Token", command=authorize_xbox_token, width=300)
button_authorize.pack(pady=10)

button_authorize = customtkinter.CTkButton(app, text="Check XBL Token", command=check_token, width=300)
button_authorize.pack(pady=10)

tabview = customtkinter.CTkTabview(app, width=800, height=200)
tabview.pack(padx=20, pady=20)

tabview.add("Page 1")  
tabview.add("Page 2")
tabview.add("Page 3")  
tabview.set("Page 1") #default page 1

#buttons for tab's below
invite = customtkinter.CTkButton(tabview.tab("Page 1"), text="Invite Spam (Coming Soon)", width=500)
invite.pack(pady=10)

button2 = customtkinter.CTkButton(tabview.tab("Page 1"), text="Spoof Games (Coming Soon)", width=500)
button2.pack(pady=10)

button3 = customtkinter.CTkButton(tabview.tab("Page 1"), text="Gamertag To XUID (Coming Soon)", width=500)
button3.pack(pady=10)

button4 = customtkinter.CTkButton(tabview.tab("Page 2"), text="Coming Soon....", width=500)
button4.pack(pady=10)

button5 = customtkinter.CTkButton(tabview.tab("Page 2"), text="Coming Soon....", width=500)
button5.pack(pady=10)

button6 = customtkinter.CTkButton(tabview.tab("Page 2"), text="Coming Soon....", width=500)
button6.pack(pady=10)

button7 = customtkinter.CTkButton(tabview.tab("Page 3"), text="Coming Soon....", width=500)
button7.pack(pady=10)

button8 = customtkinter.CTkButton(tabview.tab("Page 3"), text="Coming Soon....", width=500)
button8.pack(pady=10)

button9 = customtkinter.CTkButton(tabview.tab("Page 3"), text="Coming Soon....", width=500)
button9.pack(pady=10)


label = customtkinter.CTkLabel(app, text="Terminal Output Below", fg_color="transparent", width=10, height=10)
label.pack(pady=10)

output = customtkinter.CTkTextbox(app, width=800, height=200, corner_radius=5)
output.insert("0.0", "Everything will output here...." * 1)  
output.pack(padx=20, pady=20)  

app.mainloop()
