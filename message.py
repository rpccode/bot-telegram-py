from config import *  # importamos el token
from twilio.rest import Client

client = Client(account_sid, auth_token)


def enviar_whatsapp(message):
    message = client.messages.create(
        from_=fromnum,
        body=message,
        to='whatsapp:+18299785120'
    )

    print(message.sid)


def enviar_whatsapp_to(message, to):
    message = client.messages.create(
        from_=fromnum,
        body=message,
        to=f'whatsapp:+1{to}'
    )

    print(message.sid)
