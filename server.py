
from flask import Flask, request
from twilio import twiml
import re
from twilio.rest import TwilioRestClient
import time
import merch
t=time.strftime("%d-%m-%Y %H:%M")
client = TwilioRestClient(account='ACb99e1eafaf2f4640d837cd04677524c7', token='2909dd93eb745de3778f22b08af829c8')
app = Flask(__name__)


@app.route('/sms', methods=['POST'])
def sms():
	print "REquest received"
	number = request.form['From']
	message_body = request.form['Body']
	f=open('user.dat','r')
	nl=[]
	lis=[]
	for line in f:
		lis=line.split()
		if number==lis[0]:
			m=re.search('(\d+)-(\d+)',message_body)
			val= m.group(1)
			val1= m.group(2)
			sender=lis[1]
			rec=val
			val=val[:2] + 'K-' + val[2:]
			lis[2]=str(int(lis[2])-int(val1))
		nl.append(lis)
	f.close()
	f=open('user.dat','w')
	for lis in nl:
		for i in lis:
			f.write(i)
			f.write('\t')
		f.write('\n')
	f.close()
	print val1,val
	numb=merch.incr_mer(str(val1),str(rec))
	mes=str(t)+"\nYou paid Rs."+str(val1)+" to KA-"+str(val)
	mg="Your account was credited with:"+str(val1)+" from:"+str(sender)
	client.messages.create(from_='+12105260549',
                       to=number,
                       body=mes)
	client.messages.create(from_='+12105260549',
                       to=numb,
                       body=mg)
	resp = twiml.Response()
	resp.message('Hello, you paid: {}, to: KA-{}'.format(val1, val))
	return str(mes)
 
if __name__ == '__main__':
	app.run()
