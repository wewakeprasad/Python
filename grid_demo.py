import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
            from_email='wewakeprasad@gmail.com',
                to_emails='wewakeprasad@gmail.com',
                    subject='Life is tough',
                        html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
        sg = SendGridAPIClient(os.environ.get('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'))
            response = sg.send(message)
                print(response.status_code)
                    print(response.body)
                        print(response.headers)
except Exception as e:
        print(str(e))

