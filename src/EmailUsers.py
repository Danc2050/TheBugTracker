import yagmail


class EmailUsers:
    def __init__(self, username, password):
        try:
            self.yag = yagmail.register(username, password)
            self.yag = yagmail.SMTP(username)
        except Exception as e:
            raise Exception("Unable to initialize email credentials: " + str(e))

    # sends email to given user 'to_send'
    def send_email(self,
                   body,
                   subject,
                   to_send):
        try:
            self.yag.send(to_send, subject, body)
        except yagmail.error.YagAddressError as e:
            raise Exception("Address given is in an invalid format with exception: " + str(e))
        except yagmail.error.YagInvalidEmailAddress as e:
            raise Exception("Email address does not exist. exception: " + str(e))

    # sends email to self
    def email_self(self,
                   body,
                   subject):
        try:
            self.yag.send(contents=[body], subject=[subject])
        except TypeError as e:
            raise Exception("Type mismatch. Contents may be a string, dictionary, file, or HTML. exception: " + str(e))
