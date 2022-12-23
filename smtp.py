import smtplib
from email.message import EmailMessage
from message import *
from config import *


def email_registro(email):
    enviar_whatsapp("Confimacion de Registro: Se a registrado con exito a Tienda La essperanza bot")
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


def email_cancelacion_orden(email, producto):
    email_subject = "Confimacion de Cancelacion de la Orden"
    receiver_email_address = email  # "rperezcasilla@gmail.com"
    # Create an email message object
    message = EmailMessage()

    # Read file containing html
    # with open('registeMessage.html', 'r') as file:
    #     file_content = file.read()

    texto = f'La Orden {producto[0]} a sido cancelada con exito!'
    # texto += '<p>  </p>'
    # texto += f'Orden #:<p>{producto[0]}</p>\n\n '
    # texto += f'<p>Direccion de Envio: </p>{producto[1]}\n'
    # texto += f'<p>Metodo de Envio: </p>{producto[2]}\n'
    # texto += f'<p>Sub Total: </p>{producto[3]}\n'
    # texto += f'<p>Impuesto: </p>{producto[4]}$\n'
    # texto += f'<p>Cargo de envio: </p>{producto[5]}\n'
    # texto += f'<p>Monto Total: </p>{producto[6]}\n'
    # texto += '<img src="" alt="" >'

    enviar_whatsapp(texto)

    # Configure email headers
    message['Subject'] = email_subject
    message['From'] = sender_email_address
    message['To'] = receiver_email_address

    # Add message content as html type
    message.set_content(texto)

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
