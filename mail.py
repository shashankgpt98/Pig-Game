import smtplib #Importing smtp library
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# we are using google mails( XXXX@gmail.com )
MY_ADDRESS = 'Your email'
PASSWORD = 'Your PASSWORD'



"""Reading name and email address (to which we want to send mail) from 
txt file and stored in corresponding array"""

def get_contacts(info): # creating get_contacts function to do above commented work
	name=[]
	email=[]
	with open(info,mode='r') as details:
		for i in  details:
			name.append(i.split()[0])
			email.append(i.split()[1])
	return name,email   

""" txt file contain name space email
******* do not give space between name itself """



# main function
def main():
	name , email = get_contacts('info.txt') # calling get_contacts function
	
	s=smtplib.SMTP('smtp.gmail.com',587) #calling smtp gmail server , port = 587
	s.ehlo() # extended hello(ehlo) to check whether connection stabilised or not
	
	s.starttls() #Put the SMTP connection in TLS (Transport Layer Security) mode
	# it secure the connection
	s.ehlo()
	
	# login to your account 
	s.login(MY_ADDRESS, PASSWORD)
	
	""" n points name and e points email form name and email list"""
	for n,e in zip(name,email):
		msg= MIMEMultipart()
		message = "Hi " + n+"," "\n This mail is send via Python." 
		# print(message)
		
		msg['From']=MY_ADDRESS
		msg['To']=e
		msg['Subject']="Read This :)"
		msg.attach(MIMEText(message, 'plain'))
		s.send_message(msg)
		del msg
	s.quit() # Terminate the SMTP session and close the connection

if __name__ == '__main__':
    main()