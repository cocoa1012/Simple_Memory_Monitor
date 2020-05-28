import subprocess
import os
import sys
import time
import datetime
#Gmail and SMTP
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import smtplib

# Get email info
try:
	senderInfo = open("sender.list","r")
except Exception as e:
	print (e)
	print ("Can not open sender.list")
	exit(2)
try:
	receiverInfo = open("receiver.list","r")
except Exception as e:
	print (e)
	print ("Can not open receiver.list")
	exit(2)
# clean email info
sender = senderInfo.readline().strip("\r\n")
passwd = senderInfo.readline().strip("\r\n")
receiverSize = int(receiverInfo.readline().strip("\r\n"))
receivers = [receiverInfo.readline().strip("\r\n") for i in range(receiverSize)]
emails = [elem.strip().split(',') for elem in receivers]

# define paras
# mem size in MB
mem_threshold = 4000
# interval in sec
detect_interval = 3600


def check_mem(threshold):
	# command for checking memory
	cmd = "vmstat -S M | awk 'NR==3{print $4}' | xargs"
	# result in MB
	mem_remaining = subprocess.check_output(cmd, shell=True)
	# clean output
	mem_remaining = mem_remaining.decode("utf-8").strip()
	print (mem_remaining)
	if (int(mem_remaining) < threshold):
		return True
	else:
		return False

	

def send_email_byGmail(subject, message):
	global sender, passwd, receivers, emails
	
	msg = MIMEMultipart()
	msg['Subject'] = subject
	msg['From'] = sender
	msg['To'] = ','.join(receivers)
	msg.preamble = 'Multipart massage. \n'
	part = MIMEText(message)
	msg.attach(part)
	try:
		smtp = smtplib.SMTP("smtp.gmail.com:587")
		smtp.ehlo()
		smtp.starttls()
		smtp.login(sender, passwd)
		smtp.sendmail(msg['From'], emails, msg.as_string())
		print ("Send mails to", msg["To"])
	except Exception as e:
		print (e)
		print ("Can not send email!")

while True:
	print ("Start detection!")
	print ("Current time: %s" % datetime.datetime.now())
	if (check_mem(mem_threshold)):
		print("WARNING: Low memory detected!")
		send_email_byGmail("Server memory unusual!", "There may be some processes consume too much memory!")
	else:
		print("OK: Memory is normal.")
	print("------------------------------------------")
	time.sleep(detect_interval)
