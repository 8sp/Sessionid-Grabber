# Copyright (c) 2022 All Rights Reserved / Null
# YouTube Mp3 Downloader Developed & Programmed By Null
# Gain our Friendsip - @entrysquad (IG) @overexcited (T)

# Libraries
import requests
import os
import colorama
from colorama import Fore
from os import system
colorama.init(autoreset=True)
system("title " + "Sessionid Grabber - By Null")

r1 = requests.session() 
imz = { 
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
    'accept-encoding': 'gzip, deflate, br', 
    'accept-language': 'en-US,en;q=0.9', 
    "cookie": "ig_did=0897491F-B736-4E7E-A657-37438D0967B8; csrftoken=xvAQoMiz2eaU4RrcmRp2hqinDVMfgkpe; rur=FTW; mid=XxTPfgALAAGHGReE-x_i1ISMG4Xr", 
    'sec-fetch-dest': 'document', 
    'sec-fetch-mode': 'navigate', 
    'sec-fetch-site': 'none', 
    'sec-fetch-user': '?1', 
    'upgrade-insecure-requests': '1', 
    'user-agent': 'Mozilla/5.2 (Linux; Android 6.3; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Mobile Safari/537.36' 
}

# Null
logo = f"""     
     __       _ _ 
  /\ \ \_   _| | |
 /  \/ / | | | | |
/ /\  /| |_| | | |
\_\ \/  \__,_|_|_| {Fore.WHITE}(v1.0){Fore.RESET}

"""
print(Fore.CYAN+logo)

# Username & Password
def login(): 
    global csrftoken , username 
    global ds 
    global sessionid 
    login_url = 'https://www.instagram.com/accounts/login/ajax/' 
    def user_pass(): 
        global username,password 
        username = input(f"[{Fore.MAGENTA}?{Fore.RESET}] Username: ") 
        password = input(f"[{Fore.MAGENTA}?{Fore.RESET}] Password: ") 
    user_pass() 
    login_headers = { 
        "accept": "*/*", 
        "accept-encoding": "gzip, deflate, br", 
        "accept-language": "en-US,en;q=0.9", 
        "content-length": "267", 
        "content-type": "application/x-www-form-urlencoded", 
        "cookie": "ig_did=0897491F-B736-4E7E-A657-37438D0967B8; csrftoken=xvAQoMiz2eaU4RrcmRp2hqinDVMfgkpe; rur=FTW; mid=XxTPfgALAAGHGReE-x_i1ISMG4Xr", 
        "origin": "https://www.instagram.com", 
        "referer": "https://www.instagram.com/", 
        "sec-fetch-dest": "empty", 
        "sec-fetch-mode": "cors", 
        "sec-fetch-site": "same-origin", 
        "user-agent": F"Mozilla/91.81 (Linux; Android 6.3; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Mobile Safari/537.36", 
        "x-csrftoken": "xvAQoMiz2eaU4RrcmRp2hqinDVMfgkpe", 
        "x-ig-app-id": "1217981644879628", 
        "x-ig-www-claim": "0", 
        "x-instagram-ajax": "180c154d218a", 
        "x-requested-with": "XMLHttpRequest"} 
    login_data = { 
        "username": username, 
        "enc_password": '#PWD_INSTAGRAM_BROWSER:0:&:' + password} 
# Inc. Password
    def login2(): 
        global ig_did, csrftoken, sessionid 
        login2 = r1.post(login_url, data=login_data, headers=login_headers) 
        if '2 secure acc' in login2.text: 
            print(f"[{Fore.RED}-{Fore.RESET}] Incorrect Password")
            quit() 
        if login2.content == b'{"user": false, "authenticated": false, "status": "ok"}': 
            print(f"[{Fore.RED}-{Fore.RESET}] Incorrect Username") 
            quit() 
        elif ('showAccountRecoveryModal') in login2.text: 
            print(f"[{Fore.RED}-{Fore.RESET}] Incorrect Password") 
            quit() 
        elif ('{"message": "checkpoint_required"') in login2.text:  
            print(f"[{Fore.MAGENTA}1{Fore.RESET}] Close Swap") 
            print(f"[{Fore.MAGENTA}2{Fore.RESET}] ReTry") 
            print(f"[{Fore.MAGENTA}3{Fore.RESET}] Email/PhoneNumber Code") 
            print(f"[{Fore.MAGENTA}3{Fore.RESET}] About Developer")
            choose = input(f"{Fore.MAGENTA}>{Fore.RESET} ") 
            if choose == '1': 
                quit() 
            elif choose == '2': 
                return login2() 
            elif choose == '3': 
                z = login2.json() 
                r = z['checkpoint_url'] 
                v = 'https://www.instagram.com'+r+'?__a=1' 
                s = r1.get(v,headers=imz).text 
            elif choose == '4':
                print("Developed By Null, t.me/overexcited")
            try: 
                email = re.findall('"email":"(.*?)"', s) 
                print(f"[{Fore.GREEN}+{Fore.RESET}] Email: {email}") 
                phone = re.findall('"phone_number":"(.*?)"', s) 
                print(f"[{Fore.GREEN}+{Fore.RESET}] PhoneNumber: "+email) 
            except: 
                pass 
            y = input("[{Fore.RED}1{Fore.RESET}] Email - [{Fore.RED}2{Fore.RESET}] Phone Number: ") 
            if y == '1': 
                send_email = r1.post(v, headers=login_headers, data={ 
                    'choice': '1' 
                }, cookies=login2.cookies) 
                if 'sent to the email address' in send_email.text:print("Sent To Email") 
            elif y == '2': 
                sent_email = r1.post(v, headers=login_headers, data={ 
                    'choice': '0' 
                }, cookies=login2.cookies) 
                print(sent_email.text) 
            seccode = input(f"SecurityCode: ") 
            b = r1.post(v, headers=login_headers, data={ 
                'security_code': f'{seccode}' 
            }, cookies=login2.cookies) 
            if '"status": "ok"' in b.text: 
                login2() 
            else: 
                print(f"[{Fore.RED}!{Fore.RESET}] Error, Please Secure Our Login Attemp") 
                quit() 
        elif 'userId' in login2.text: 
            print(f"[{Fore.GREEN}+{Fore.RESET}] Successfully Logged In >> @"+username+"") 
            ds = login2.cookies['ds_user_id'] 
            csrftoken = login2.cookies['csrftoken'] 
            sessionid = login2.cookies['sessionid'] 
            print(f"[{Fore.GREEN}+{Fore.RESET}] Sessionid: "+sessionid) 
        else: 
            print(login2.text) 
            quit() 
    login2() 
login()
# End /
