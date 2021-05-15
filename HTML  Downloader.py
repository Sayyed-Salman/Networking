import urllib.request
import webbrowser
import socket
import re


print("HTML-Downloader")

print("-"*52)

FORMAT = "utf-8"
URL =  urllib.request.urlopen(input("Enter Website URL:"))
url = URL.geturl()

name = url.split('/')
webstring = name[2]


IP = socket.gethostbyname(webstring)

BYTEcode = URL.read()
D = BYTEcode.decode(FORMAT)

URL.close()
#print("WEBSITE URL: ",URL.geturl())
print("WEBSITE NAME:",webstring)
print("IP-ADDRESS:",IP)
print()

NAME = f"HTMLof-{webstring}.txt"
with open(NAME,"w+",encoding = 'utf-8') as out:
    out.seek(0)
    out.write("<!--\n")
    out.write(f"""
WEBSITE URL: {url}\n
IP ADDR:{IP}\n
WEBSITE NAME:{webstring}\n""")
    out.write("-->\n")
    out.write(D)
    out.close()

print("WEBSITE CODE SAVED...")

val = ""
while val == "":
    val=input("OPEN IN BROWSER(Y/N): ")
    if val == "Y":
        webbrowser.open(URL.geturl(),new =5)
    elif val == "y":
        webbrowser.open(URL.geturl(),new =5)
    else:
        break
    

print("DONE")

