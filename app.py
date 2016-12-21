#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    speech = "Webhook work ery well !good luck"

    print("Response:")
    print(speech)

    slack_message = {
        "text": speech,
        {
        "attachments": [
            {
                "fallback": "New ticket from Andrea Lee - Ticket #1943: Can't rest my password - https://groove.hq/path/to/ticket/1943",
                "pretext": "New ticket from Andrea Lee",
                "title": "Ticket #1943: Can't reset my password",
                "title_link": "https://groove.hq/path/to/ticket/1943",
                "text": "Help! I tried to reset my password but nothing happened!",
                "color": "#7CD197"
            }
         ]
       }
     }

    print(json.dumps(slack_message))

    res= {
        "speech": speech,
        "displayText": speech,
        "data": {"slack": slack_message},
        # "contextOut": [],
        "source": "apiai-weather-webhook-sample"
    }


    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

     # print(json.dumps(item, indent=4))


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=False, port=port, host='0.0.0.0')
