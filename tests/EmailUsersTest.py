from src.EmailUsers import EmailUsers


class testEmailUsers:
    def __init__(self):
        print("testing")

    def testInit(self, username, password):
        """
        WHAT IT DOES:
            - Tests init for clearance
            - yag.register function initializes keyring module to set Gmail credentials
            - yag.SMPT function initializes server connection
        CASES:
            PASS:
                - Gmail username-password combo provided is valid
                - and Gmail account cleared for authorization
            FAIL:
                - Gmail username-password combo is not valid
                - Gmail username-password combo has bad credentials
                - Gmail account does not allow Less Secured Apps
        """
        EmailUsers(username, password)


    def testSendEmail(self, username, password):
        """
        WHAT IT DOES:
            - Tests send email functionality
            - The yag.send function takes in the parameters:
                - the email's body
                - the email's subject
                - the receiver's email (does not have to be gmail)
        CASES:
            PASS:
                - Valid credentials of sender and receiver
            FAIL:
                - Invalid credentials of sender and receiver
        """
        test = EmailUsers(username, password)
        body = "This is a test body"
        subject = "This is a test subject"
        to_send = input("to send: ")
        test.send_email(body, subject, to_send)


    def testEmailSelf(self, username, password):
        """
                WHAT IT DOES:
                    - Tests send email TO SELF functionality
                    - The yag.send function takes in the parameters:
                        - the lack of a receiving email will make function send email to sender
                        - the email's body (contents)
                        - the email's subject (subject)
                CASES:
                    PASS:
                        - Valid credentials of sender
                    FAIL:
                        - Invalid credentials of sender
                """
        test = EmailUsers(username, password)
        body = "This is a test body"
        subject = "This is a test subject"
        test.email_self(body, subject)


    def run(self):
        username = input("username: ")
        password = input("password: ")
        self.testInit(username, password)
        self.testSendEmail(username, password)
        self.testEmailSelf(username, password)


if __name__ == '__main__':
    test_run = testEmailUsers()
    test_run.run()
