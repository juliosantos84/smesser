import argparse
from twilio_client.client import TwilioClient

parser = argparse.ArgumentParser(
    prog        = 'smstoolkit',
    description = 'Does stuff with SMS using Twilio.Configure TWILIO_ACCOUNT_SID TWILIO_AUTH_TOKEN and TWILIO_MESSAGING_SERVICE_SID')
parser.add_argument('command', type=str, default="send", choices=['send'])
parser.add_argument('-t', '--to', type=str, default='+12016745097')
parser.add_argument('-b', '--body', type=str, default='Hello, is it me you\'re looking for?')
args = parser.parse_args()

if args.command == 'send':
    client = TwilioClient()
    body = args.body
    to = args.to
    client.send(body, to)
    