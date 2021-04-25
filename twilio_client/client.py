import argparse
from twilio.rest import Client
import os

class TwilioClient:
    def __init__(self):
        self.client = Client()
        self.messaging_service_sid = os.getenv("TWILIO_MESSAGING_SERVICE_SID")
        self.from_phone_number = os.getenv("TWILIO_FROM_PHONE_NUMBER")

    def send(self, body, to):
        print ("Sending the message {} to {}".format(body, to))
        message = self.client.messages.create(
            messaging_service_sid = self.messaging_service_sid,
            body = body,
            to = to,
            from_ = self.from_phone_number
        )
        print ("Sent message. message.sid={}".format(message.sid))