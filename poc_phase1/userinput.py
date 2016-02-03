import getpass
from validate_email import validate_email

class Input(object):

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

    def getProcessInputs(self):

        Useremail = self.input_email()
        password = self.input_password()
        return Useremail, password

    def getUserTimeFrame(self):
        
        days = int(raw_input("Enter Time Duration in Days: "))
        print "\nPlease wait ...processing\n"
        return days




