import smtplib
from email.message import EmailMessage
from config import *


def email_registro(email):
    email_subject = "Confimacion de Registro"
    receiver_email_address = email  # "rperezcasilla@gmail.com"
    # Create an email message object
    message = EmailMessage()

    # Read file containing html
    with open('registeMessage.html', 'r') as file:
        file_content = file.read()

    # Configure email headers
    message['Subject'] = email_subject
    message['From'] = sender_email_address
    message['To'] = receiver_email_address

    # Add message content as html type
    message.set_content(file_content, subtype='html')

    # Set smtp server and port
    server = smtplib.SMTP(email_smtp, '587')

    # Identify this client to the SMTP server
    server.ehlo()

    # Secure the SMTP connection
    server.starttls()

    # Login to email account
    server.login(sender_email_address, email_password)

    # Send email
    server.send_message(message)

    # Close connection to server
    server.quit()


def email_cancelacion_orden(email):
    email_subject = "Confimacion de Cancelacion de la Orden"
    receiver_email_address = email  # "rperezcasilla@gmail.com"
    # Create an email message object
    message = EmailMessage()

    # Read file containing html
    with open('registeMessage.html', 'r') as file:
        file_content = file.read()

    # Configure email headers
    message['Subject'] = email_subject
    message['From'] = sender_email_address
    message['To'] = receiver_email_address

    # Add message content as html type
    message.set_content(file_content, subtype='html')

    # Set smtp server and port
    server = smtplib.SMTP(email_smtp, '587')

    # Identify this client to the SMTP server
    server.ehlo()

    # Secure the SMTP connection
    server.starttls()

    # Login to email account
    server.login(sender_email_address, email_password)

    # Send email
    server.send_message(message)

    # Close connection to server
    server.quit()

    def email_confimacion_orden(email):
        email_subject = "Confimacion de Orden"
        receiver_email_address = email  # "rperezcasilla@gmail.com"
        # Create an email message object
        message = EmailMessage()

        # Read file containing html
        with open('registeMessage.html', 'r') as file:
            file_content = file.read()

        # Configure email headers
        message['Subject'] = email_subject
        message['From'] = sender_email_address
        message['To'] = receiver_email_address

        # Add message content as html type
        message.set_content(file_content, subtype='html')

        # Set smtp server and port
        server = smtplib.SMTP(email_smtp, '587')

        # Identify this client to the SMTP server
        server.ehlo()

        # Secure the SMTP connection
        server.starttls()

        # Login to email account
        server.login(sender_email_address, email_password)

        # Send email
        server.send_message(message)

        # Close connection to server
        server.quit()
