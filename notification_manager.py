from twilio.rest import Client

TWILIO_SID = 'AC80796c0ac4f5022fc222942a1fb60995'
TWILIO_AUTH_TOKEN = 'c39346d44e7dffc99720241354273360'
TWILIO_VIRTUAL_NUMBER = '+17627222683'
TWILIO_VERIFIED_NUMBER = '+918946800111'


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)