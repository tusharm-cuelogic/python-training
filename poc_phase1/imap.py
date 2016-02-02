from userinput import Input
import imaplib
import process_emails
import datetime

userInputs = Input()
Useremail = userInputs.input_email()
password = userInputs.input_password()

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(Useremail, password)
mail.list()


current_date = datetime.date.today().strftime("%d-%b-%Y")
previous_date = (datetime.date.today() - datetime.timedelta(10)).strftime("%d-%b-%Y")

send_emails_list, total_send_email = process_emails.FilterSendEmails(mail, current_date, previous_date)
rec_emails_list, total_rec_email = process_emails.FilterRecEmails(mail, current_date, previous_date)

process_emails.filtertopemails(send_emails_list, total_send_email, 'send')
process_emails.filtertopemails(rec_emails_list, total_send_email, 'rec')