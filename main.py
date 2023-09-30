import argparse
import smtplib
import time
import urllib3
from lxml import html
import telebot



parser = argparse.ArgumentParser()

parser.add_argument("--price",type=str,required=True)
parser.add_argument("--link",type=str,required=True)
parser.add_argument("--timeout",type=int,required=True)
parser.add_argument("--test",action="store_true",required=False)
args = parser.parse_args()
#print(args)

try:
    f=open("email.txt","r")
    lines=f.readlines()
    email=str(lines[0].replace("\n",""))
    password=str(lines[1].replace("\n",""))
    f.close()
except:
    print("Email not found")
    email=""
    password=""
try:
    f=open("telegram.txt","r")
    lines=f.readlines()
    token=lines[0].replace("\n","")
    chatid=lines[1].replace("\n","")
    f.close()
except:
    print("Telegram not found")
    token=""
    chatid=""

if email=="" and password=="" and token=="" and chatid=="":
    raise Exception("No notification system inserted")

if "&" in args.link:
    raise Exception("Wrong link format. Check the & ...")


bot = telebot.TeleBot(token, parse_mode=None)


def getNameAndPriceFirstArticle():
    r = http.request('GET', link)
    data_string = r.data.decode('utf-8', errors='ignore')
    tree = html.fromstring(data_string)
    tree=tree.xpath("//div[@class='SmallCard-module_item-key-data__fcbjY']")
    data=list(tree[0].itertext())
    if data[-1]=="Venduto":
        name=data[0]
        price=data[1]
    else:
        name=data[0]
        price=data[-2]
    return name,price


min,max=args.price.split(",")
link = args.link+"&qso=true&shp=true&order=datedesc&ps="+str(min)+"&pe="+str(max)


def send_email(name,price):
    messaggio = name+"\n"+str(price)+"\nLink:\n"+link
    service_email = smtplib.SMTP("smtp-mail.outlook.com", 587)
    service_email.ehlo()
    service_email.starttls()
    service_email.login(email,password)
    service_email.sendmail(email,email,('Subject: Subito.it List Updated\n\n ' + messaggio).encode('utf-8'))
    service_email.quit()

if args.test:
    send_email("TEST","NOTIFICATION")
    bot.send_message(chatid,"TEST NOTIFICATION: "+link)
    quit()

http = urllib3.PoolManager()

firstArticle=getNameAndPriceFirstArticle()
print("First product: "+firstArticle[0]+", price "+str(firstArticle[1]))
lastArticle = ""
richieste = 0
while True:
    try:
        richieste += 1
        print("Request : ", richieste)
        lastArticle = firstArticle
        firstArtice = getNameAndPriceFirstArticle()
        if (firstArticle != lastArticle):
            name=firstArticle[0]
            price = firstArticle[1]
            print("New item")
            print(price)
            print(len(price))
            if token!="" and chatid!="":
                bot.send_message(chatid,name+"\n"+price[:-2]+" euro\nNew item: "+link)
            if email!="" and password!="":
                send_email(name,price[:-2]+" euro")
            
        else:
            time.sleep(args.timeout*60)
    except Exception as e:
        print(e)
        time.sleep(5)



