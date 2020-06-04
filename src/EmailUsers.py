import yagmail


class EmailUsers:
    def __init__(self):
        # yagmail.SMTP() without parameters will attempt to locate a .yagmail file in the home directory
        # that contains the gmail username. Should be used in the future to avoid having
        # credentials placed in code
        self.yag = yagmail.SMTP()
        # yag = yagmail.SMTP()
        # another workaround is to call yagmail.register('gmail', 'password') once and have it registered
        # via the keyring library

    # sends email to given user 'to_send'
    def send_email(self,
                   body,
                   subject,
                   to_send):
        try:
            self.yag.send(to_send, subject, body)
            print("Email sent to", to_send)
        except:
            print("Something went wrong")

    # sends email to self
    def email_self(self,
                   body,
                   subject):
        try:
            self.yag.send(contents=[body], subject=[subject])
            # yag.send with no specified user will default to sending the email to yourself (registered user)
            print("email sent to self")
        except:
            print("Something went wrong")
