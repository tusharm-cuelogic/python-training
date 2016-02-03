from email.parser import Parser
from email.utils import parseaddr

def filterSendEmails(mail, current_date, previous_date):

	send_emails_dict = {}

	mail.select('[Gmail]/Sent Mail') # connect to Sentbox.
	result, data = mail.uid('search', None, '(SENTSINCE {previous_date} SENTBEFORE {current_date})'.format(previous_date=previous_date, current_date=current_date))

	total_send_email = len(data[0].split())
	#print "Total Emails Sent---->>",total_send_email

	for num in data[0].split()[::-1]:
		result, data = mail.uid('fetch', num, '(RFC822)')
		
		for msg in data[0]:

			headers = Parser().parsestr(msg)
			
			if headers['to'] != "":

				if headers['to'] in send_emails_dict:
					send_emails_dict[headers['to']] = send_emails_dict[headers['to']] + 1
				else:
					send_emails_dict[headers['to']] = 1
	#print send_emails_dict
	return 	send_emails_dict, total_send_email

def filterRecEmails(mail, current_date, previous_date):

	rec_emails_dict = {}

	mail.select('INBOX') # connect to inbox.
	result, data = mail.uid('search', None, '(SENTSINCE {previous_date} SENTBEFORE {current_date})'.format(previous_date=previous_date, current_date=current_date))

	total_rec_email = len(data[0].split())
	#print "Total Emails Rec---->>",total_rec_email
	for num in data[0].split()[::-1]:
		result, data = mail.uid('fetch', num, '(RFC822)')

		for msg in data[0]:

			headers = Parser().parsestr(msg)
			
			if headers['from'] != "":

				if headers['from'] in rec_emails_dict:
					rec_emails_dict[headers['from']] = rec_emails_dict[headers['from']] + 1
				else:
					rec_emails_dict[headers['from']] = 1
	#print rec_emails_dict
	return 	rec_emails_dict, total_rec_email


def filtertopemails(emails_list, total_emails, email_type):
	
	if email_type == "send": 
		print "\n* Total number Of Sent Emails: %d\n" % total_emails
	else:
		print "* Total number Of Receive Emails: %d\n" % total_emails

	print "{0:40} {1:40} {2:10} {3:10}\n".format('Name', 'Email', 'Percentage', 'Emails Count')
	#print "{0:40} {1:40} {2:10}\n".format('Name', 'Email', 'Percentage')

	#for email, count in emails_list.items():
	icount = 0
	for email, count in sorted(emails_list.iteritems(), key=lambda (k,v): (v,k))[::-1]:
	#for email, count in emails_list.iteritems()[::-1]:
		
		if icount <= 10:
			user_detail = parseaddr(email)
			percentage = (count/float(total_emails)) * 100
			
			if user_detail[0] != "" and user_detail[1] !="":
				#print "%s\t %s\t %s\%" % (user_detail[0], user_detail[1], round(percentage, 2))
				print '{0:40} {1:40} {2:10}% {3:10}'.format(user_detail[0], user_detail[1], round(percentage, 2), count)
				#print '{0:40} {1:40} {2:10}%'.format(user_detail[0], user_detail[1], round(percentage, 2))
		icount += 1


	print "\n===========================================================================\n"