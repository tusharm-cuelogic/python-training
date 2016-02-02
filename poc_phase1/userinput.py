import getpass
from validate_email import validate_email

class Input(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def input_email(self):
        email = raw_input("Email: ")
        is_valid = validate_email(email,verify=True)
        
        if is_valid:
            return email
        else:
            print "Please enter valid email"
            self.input_email()

    def input_password(self):
        password = getpass.getpass("Password: ")
        if password == "":
            print "Please enter password"
            self.input_password()
        else:
            return password



