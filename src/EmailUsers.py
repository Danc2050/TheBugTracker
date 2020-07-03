import yagmail
from decouple import config


class EmailUsers:
    def __init__(self):
        username = config('USER')
        password = config('KEY')
        self.yag = yagmail.register(username, password)
        self.yag = yagmail.SMTP(username)

    # sends email to given user 'to_send'
    def send_email(self,
                   body,
                   subject,
                   to_send):
        try:
            self.yag.send(to_send, subject, body)
        except yagmail.error.YagAddressError as e:
            print("Address given is in an invalid format with exception: " + str(e))
        except yagmail.error.YagInvalidEmailAddress as e:
            print("Email address does not exist. exception: " + str(e))

    # sends email to self
    def email_self(self,
                   body,
                   subject):
        try:
            self.yag.send(contents=[body], subject=[subject])
        except TypeError as e:
            print("Type mismatch. Contents may be a string, dictionary, file, or HTML. exception: " + str(e))


