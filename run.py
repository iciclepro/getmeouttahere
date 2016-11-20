
from flask import Flask, request, redirect
import twilio.twiml
from twilio.rest import TwilioRestClient

app = Flask(__name__)

my_number = "+13127213328"
account = "ACa15d8ba9789c78eb3cf5d99c5da338d7"
token = "fd92471e9fc6108bdc2aca3d83bbfdce"
client = TwilioRestClient(account, token)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""

    contacts = {'Bobby': '+12172122018', 'Jimmy':'+13123132182', 'kengyon': '+12172073302', 'tom':'+12172073270'}

    from_number = request.values.get('From',None)
    msg_body = request.values.get('Body',None)

    call = client.calls.create(to=my_number,  # Any phone number
                           from_=contacts['Bobby'], # Must be a valid Twilio number
                           url="https://handler.twilio.com/twiml/EH9d411a9f08f83938e38342c72724094f")

    resp = twilio.twiml.Response()

    for contact, num in contacts.items():
    	if contact == 'Bobby':
            resp.message("DUDE WTH YOUR HOUSE IS ON FIRE", to=my_number, sender= contacts[contact])
    	elif contact == 'Jimmy':
            resp.message("you gotta need to come home now", to=my_number,sender= contacts[contact])
    	elif contact == 'kengyon':
            with resp.message("ohmygosh our house is burning up", to=my_number, sender= contacts[contact]) as m:
                m.media("http://i.giphy.com/DFSfJcZhXcehW.gif")
    	else:
            with resp.message("Save meeeeee!!!!", to=my_number, sender= contacts[contact]) as m:
                m.media("http://i.giphy.com/xTiQyMTt0Bnc02PT8I.gif")  

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
