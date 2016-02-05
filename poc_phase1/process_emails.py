import email
#from email.parser import Parser
from email.utils import parseaddr
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

def filterSendEmails(mail, current_date, previous_date):

	send_emails_dict = {}

	mail.select('[Gmail]/Sent Mail') # connect to Sentbox.
	result, data = mail.uid('search', None, '(SENTSINCE {previous_date} SENTBEFORE {current_date})'.format(previous_date=previous_date, current_date=current_date))

	total_send_email = len(data[0].split())
	
	for num in data[0].split()[::-1]:
		result, data = mail.uid('fetch', num, '(RFC822)')
		
		email_body_content = ""
		for msg in data[0]:

			#headers = Parser().parsestr(msg)
			headers = email.message_from_string(msg)
			
			email_body = str(getEMailBody(headers))

			if headers['To'] != "":
				
				if headers['To'] in send_emails_dict:
					email_body_content += email_body
					send_mail_count = send_emails_dict[headers['To']][0] + 1
					send_emails_dict[headers['To']] = [send_mail_count, email_body_content]

				else:
					send_emails_dict[headers['To']] = [1, email_body]
					
	#print send_emails_dict
	return 	send_emails_dict, total_send_email

def filterRecEmails(mail, current_date, previous_date):

	rec_emails_dict = {}

	mail.select('INBOX') # connect to inbox.
	result, data = mail.uid('search', None, '(SENTSINCE {previous_date} SENTBEFORE {current_date})'.format(previous_date=previous_date, current_date=current_date))

	total_rec_email = len(data[0].split())

	for num in data[0].split()[::-1]:
		result, data = mail.uid('fetch', num, '(RFC822)')

		email_body_content = ""
		for msg in data[0]:

			#headers = Parser().parsestr(msg)
			headers = email.message_from_string(msg)
			email_body = str(getEMailBody(headers))
			
			if headers['From'] != "":

				if headers['From'] in rec_emails_dict:
					email_body_content += email_body
					rec_mail_count = rec_emails_dict[headers['From']][0] + 1
					rec_emails_dict[headers['From']] = [rec_mail_count, email_body_content]

				else:
					rec_emails_dict[headers['From']] = [1, email_body]
	
	#print rec_emails_dict
	return 	rec_emails_dict, total_rec_email


def filtertopemails(emails_list, total_emails, email_type):
	
	if email_type == "send": 
		print "\n* Total number Of Sent Emails: %d\n" % total_emails
	else:
		print "* Total number Of Receive Emails: %d\n" % total_emails

	print "{0:40} {1:40} {2:10} {3:10} {4:20}\n".format('Name', 'Email', 'Percentage', 'Emails Count', 'Sentiment')
	#print "{0:40} {1:40} {2:10}\n".format('Name', 'Email', 'Percentage')

	#for email, count in emails_list.items():
	icount = 0
	for email, count in sorted(emails_list.iteritems(), key=lambda (k,v): (v,k))[::-1]:
	#for email, count in emails_list.iteritems()[::-1]:

		if icount <= 10:
			user_detail = parseaddr(email)
			percentage = (count[0]/float(total_emails)) * 100
			
			if user_detail[0] != "" and user_detail[1] !="":
				#print "%s\t %s\t %s\%" % (user_detail[0], user_detail[1], round(percentage, 2))
				text_sentiment = textAnalysis(count[1].decode('utf-8').strip())
				print '{0:40} {1:40} {2:10}% {3:10} {4:20}'.format(user_detail[0], user_detail[1], round(percentage, 2), count[0], text_sentiment)
				#print '{0:40} {1:40} {2:10}%'.format(user_detail[0], user_detail[1], round(percentage, 2))
		icount += 1


	print "\n===========================================================================\n"


def textAnalysis(email_body):

	blob = TextBlob(email_body, analyzer=NaiveBayesAnalyzer())
	return blob.sentiment[0]


def getEMailBody(raw_email):

	body = ""
	if raw_email.is_multipart():
		for part in raw_email.walk():
			content_type = part.get_content_type()

			if content_type == 'text/plain':
				body += part.get_payload(decode=True)

	if body != "" :
		return body	

	
