import yagmail
from decouple import config


class EmailUsers:
    def __init__(self):
        sender = config('USER')
        key = config('KEY')
        self.yag = yagmail.register(sender, key)
        self.yag = yagmail.SMTP()
        # another workaround is to call yagmail.register('gmail', 'password') once and have it registered
        # via the keyring library

    # sends email to given user 'to_send'
    def send_email(self,
                   body,
                   subject,
                   to_send):
        try:
            self.yag.send(to_send, subject, body)
        except yagmail.error.YagAddressError:
            print("Address given is in an invalid format")
        except yagmail.error.YagInvalidEmailAddress:
            print("Email address does not exist")

    # sends email to self
    def email_self(self,
                   body,
                   subject):
        try:
            self.yag.send(contents=[body], subject=[subject])
            # yag.send with no specified user will default to sending the email to yourself (registered user)
        except TypeError:
            print("Type mismatch. Contents may be a string, dictionary, file, or HTML")

