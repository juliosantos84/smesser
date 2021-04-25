# smesser
An SMS toolkit to mess around with an aloof home repair contractor, and anyone else that annoys me :)

# requirements
- Python 3.9.1
- A Twilio account: www.twilio.com
- A desire to incessantly message an aloof contractor until they answer.  Or anyone really.

# installation
1. _Optional_ Create a virtualenv and activate it.
1. Run `./install.sh`.

# usage
Sending a message:
```python
# example 1
python app.py send -t +1234567890 -b 'Hello, remember me?'
```
```python
# example 2
python app.py send -t +1234567890 -b 'Hey, me again. When are you starting the project?'
```
