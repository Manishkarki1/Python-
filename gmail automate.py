import smtplib as s
ob=s.SMTP("smtp.gmail.com",587)
ob.ehlo()
ob.starttls()
ob.login("karkimanish411@gmail.com","Sh@re123#")
subjects="practicing python"
body="Hello good morning"
message="subject:{}\n\n{}".format(subjects,body)
listaddress=["tara9841443761@gmail.com","educationmaterial1@gmail.com"]
ob.sendmail("karkimanish411@gmail.com",listadd,message)
print("send mail")
ob.quit()