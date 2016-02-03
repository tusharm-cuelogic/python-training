from userinput import Input
import imaplib
import process_emails
import datetime

def userLogin():
	
	userInputs = Input()
	Useremail, password = userInputs.getProcessInputs()

	mail = imaplib.IMAP4_SSL('imap.gmail.com')

	try:
		mail.login(Useremail, password)
		mail.list()
		days = userInputs.getUserTimeFrame()
		processEmailsInfo(mail, days)
	except Exception:
		print "[AUTHENTICATIONFAILED] Invalid credentials"
		userLogin()


def processEmailsInfo(mail, days):
	current_date = datetime.date.today().strftime("%d-%b-%Y")
	previous_date = (datetime.date.today() - datetime.timedelta(days)).strftime("%d-%b-%Y")

	send_emails_list, total_send_email = process_emails.filterSendEmails(mail, current_date, previous_date)
	rec_emails_list, total_rec_email = process_emails.filterRecEmails(mail, current_date, previous_date)

	process_emails.filtertopemails(send_emails_list, total_send_email, 'send')
	process_emails.filtertopemails(rec_emails_list, total_rec_email, 'rec')
	

userLogin()




