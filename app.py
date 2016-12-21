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
    
    res = processRequest(req)

    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


def processRequest(req):
 
    name= req.get("result").get("parameters").get("name")
    res = makeWebhookResult(name)
    return res





def makeWebhookResult(name):
  
  



    speech = name

    print("Response:")
    print(speech)

    slack_message = {
        "text": speech,
        "attachments": [
            {
                "title": name,
                "title_link": "https://spring.io/tools/sts",
                "color": "#36a64f",

                "fields": [
                    {
                        "title": "Condition",
                        "value": name,
                        "short": "false"
                    }
                   
                ],

                "thumb_url": "https://scontent-lhr3-1.xx.fbcdn.net/v/t1.0-9/13718655_1143790748975145_2575595500054770440_n.jpg?oh=4a89371dd70b8cfe167d882da3fe6ca4&oe=58F85BFD"
            }
        ]
    }

  

    print(json.dumps(slack_message))

    return {
        "speech": speech,
        "displayText": speech,
        "data": {"slack": slack_message},
        # "contextOut": [],
        "source": "apiai-weather-webhook-sample"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=False, port=port, host='0.0.0.0')
