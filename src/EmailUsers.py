import yagmail

# yagmail.SMTP() without parameters will attempt to locate a .yagmail file in the home directory
# that contains the gmail username. Should be used in the future to avoid having
# credentials placed in code

yag = yagmail.SMTP('bugtrackerp@gmail.com', 'D@nkC0d3rs')
# yag = yagmail.SMTP()
# another workaround is to call yagmail.register('gmail', 'password') once and have it registered
# via the keyring library


# sends email to given user 'to_send'
def send_email(body,
               subject,
               to_send):
    yag.send(to_send, subject, body)
    print("Email sent to", to_send)


# sends email to self
def email_self(body,
               subject):
    yag.send(subject, body)
    # yag.send with no specified user will default to sending the email to yourself (registered user)


send_email("default bug report message", "log 0-0-0", "prikim@pdx.edu")
