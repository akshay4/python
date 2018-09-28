import smtplib
import base64 
import getpass


print("\nWelcome to Attachment Send Service ")
print("\n\nPlease Enter Your LOGIN Details - \n")

sender = input("Email Address : ")
password = getpass.getpass("Password :")

print("\n\n**********Trying to Logging You in your account*********")


try:
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    server.login(sender,password)
except Exception as e:
    print("\n\nError in Login !!",e)
    exit(0)
else:
    print("\n\n*********Your login is Sucessfull*********")


filename = input("\n\nEnter full path to your file which you want to send as attachment  \n(Remember path should be like c://some//dir//filename and that should be only text file ) - \n\n")


try:
    f = open(filename,'rb')
except Exception as e:
    print("\n\nError!! ",e)
    exit(0)
else:
    filecontent=f.read()

encodedcontent=base64.b64encode(filecontent)


n = int(input("\n\nEnter No. of RECIPIENTS - "))
print("\n\nType in RECIPIENTS Email addressess (Each in new line)\n\n")

rec = []
for i in range(n):
    rec.append(input())

rcv= ','.join(rec)

marker = "AUNIQUEMARKER"

subject = input("\n\nSubject: ")

print("\n\n****Messege - (Type EOF to quit typing)\n\n")

msg = []

while True:
    k = input()
    if k.upper() == 'EOF':
        break
    else:
        msg.append(k)

body = '\n'.join(msg)
print("\n\n***Messege is Saved ***\n\n")

header1 = """From:%s
To:%s
Subject: %s
MIME-Version: 1.0
Content-type: multipart/mixed;boundary=%s
--%s
"""%(sender,rcv,subject,marker,marker)


header2 = """Content-Type: text/plain
Content-Transfer-Encoding:8bit
%s
--%s
"""%(body,marker)
header3 = """Content-Type:  multipart/mixed;name = \"%s\"
Content-Transfer-Encoding:base64
Content-Disposition: attachment; filename=%s
%s
--%s--
"""%(filename,filename,encodedcontent,marker)
message = header1+header2+header3


print("\n\n**********Trying to send your messege with attachment********** \n\n")

try:
    server.sendmail(sender,rcv,message)
    server.close()
except Exception as e:
    print("\n\nError in Sending Mail as - \n!!",e)
    exit(0)
else:
    print("\n\nYour mail is sucessfully Delivered \n\n")
print("Thanks For using our Mail Services \n\n\n\n")
