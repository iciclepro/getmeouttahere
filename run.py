
from flask import Flask, request, redirect
import twilio.twiml
from twilio.rest import TwilioRestClient

app = Flask(__name__)

account = "ACa15d8ba9789c78eb3cf5d99c5da338d7"
token = "fd92471e9fc6108bdc2aca3d83bbfdce"
client = TwilioRestClient(account, token)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""
    #numbers = ['+12172122018','+13123132182','+12172073302']
    contacts = {'Bobby': '+12172122018', 'Jimmy':'+13123132182', 'kengyon': '+12172073302'}

    from_number = request.values.get('From',None)
    msg_body = request.values.get('Body',None)

    call = client.calls.create(to="+13127213328",  # Any phone number
                           from_=contacts['Bobby'], # Must be a valid Twilio number
                           url="https://handler.twilio.com/twiml/EH9d411a9f08f83938e38342c72724094f")

    #print (from_number)
    #print (msg_body)

    resp = twilio.twiml.Response()

    for contact, num in contacts.items():
    	if contact == 'Bobby':
            resp.message("DUDE WTH YOUR HOUSE IS ON FIRE", to='+13127213328', sender= contacts[contact])
    	elif contact == 'Jimmy':
            resp.message("you gotta need to come home now", to='+13127213328',sender= contacts[contact])
    	else:
            with resp.message("owl lol", to='+13127213328', sender= contacts[contact]) as m:
                m.media("http://i.giphy.com/DFSfJcZhXcehW.gif")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)


# Sending to my own numbeer -> how to send to others?
# Add a phone call with someone screaming
# Use giphy -> advanced shit
# 




# from twilio.rest import TwilioRestClient
# from flask import Flask, request, redirect
# import twilio.twiml

# account = "ACa15d8ba9789c78eb3cf5d99c5da338d7"
# token = "fd92471e9fc6108bdc2aca3d83bbfdce"
# client = TwilioRestClient(account, token)

# message = client.messages.create(to="2179045033", from_="3123132182",
#                                  body="Hey your house is burning down!!!")

# call = client.calls.create(to="2179045033",
#                            from_="3123132182",
#                            url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")

# client.messages.create(
#     to="+12179045033", 
#     from_="+13123132182", 
#     body="This is the ship that made the Kessel Run in fourteen parsecs?", 
#     media_url="https://c1.staticflickr.com/3/2899/14341091933_1e92e62d12_b.jpg", 
# )

# for message in client.messages.list():
#     print (message.body)

