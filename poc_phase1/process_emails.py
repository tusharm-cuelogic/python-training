from email.parser import Parser
from email.utils import parseaddr

def FilterSendEmails(mail, current_date, previous_date):

	send_emails_dict = {}

	mail.select('[Gmail]/Sent Mail') # connect to Sentbox.
	result, data = mail.uid('search', None, '(SENTSINCE {previous_date} SENTBEFORE {current_date})'.format(previous_date=previous_date, current_date=current_date))

	total_send_email = len(data[0].split())
	print "Total Sent---->>",total_send_email

	for num in data[0].split()[::-1]:
		result, data = mail.uid('fetch', num, '(RFC822)')
		
		for msg in data[0]:

			headers = Parser().parsestr(msg)
			
			if headers['to'] != "":

				if headers['to'] in send_emails_dict:
					send_emails_dict[headers['to']] = send_emails_dict[headers['to']] + 1
				else:
					send_emails_dict[headers['to']] = 1
	print send_emails_dict
	return 	send_emails_dict, total_send_email

def FilterRecEmails(mail, current_date, previous_date):

	rec_emails_dict = {}

	mail.select('INBOX') # connect to inbox.
	result, data = mail.uid('search', None, '(SENTSINCE {previous_date} SENTBEFORE {current_date})'.format(previous_date=previous_date, current_date=current_date))

	total_rec_email = len(data[0].split())
	print "Total Rec---->>",total_rec_email
	for num in data[0].split()[::-1]:
		result, data = mail.uid('fetch', num, '(RFC822)')

		for msg in data[0]:

			headers = Parser().parsestr(msg)
			
			if headers['from'] != "":

				if headers['from'] in rec_emails_dict:
					rec_emails_dict[headers['from']] = rec_emails_dict[headers['from']] + 1
				else:
					rec_emails_dict[headers['from']] = 1
	print rec_emails_dict
	return 	rec_emails_dict, total_rec_email


def filtertopemails(emails_list, total_emails, email_type):
	
	if email_type == "send": 
		print "List Of Sent Emails:"
	else:
		print "List Of Receive Emails:"

	print "Name\t Email\t Percentage\n"

	#for email, count in emails_list.items():
	count = 0
	for email, count in sorted(emails_list.iteritems(), key=lambda (k,v): (v,k)):
		
		if count <= 10:
			user_detail = parseaddr(email)
			precentage = (count/float(total_emails)) * 100

			print "%s\t %s\t %s" % (user_detail[0], user_detail[1], round(precentage, 2))
		count += 1


	print "\n===========================================================================\n"