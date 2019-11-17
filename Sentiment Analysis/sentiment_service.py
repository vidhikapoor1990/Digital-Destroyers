

from flask import Flask,jsonify
import json,requests
from flask_cors import CORS,cross_origin
from flask import json
from flask.globals import request
import ServerSettings as settings
import SentimentAnalysis
app = Flask(__name__)
CORS(app)

#------------------------------------------------------------------------------------------------------------------------

@app.route('/getSentiment', methods=['POST'])
@cross_origin()
def getCorrectSpelling():
    if request.method != 'POST':
        return json.dumps({"Status": "ERROR", "DATA": None, "Reason": "Only accept POST request"})
    if not request.headers['Content-Type'] == 'application/json':
        return json.dumps({"Status": "ERROR", "DATA": None, "Reason": "Only  accept Content-Type:application/json"})
    if not request.is_json:
        return json.dumps({"Status": "ERROR", "DATA": None,
                           "Reason": 'Expecting json data in the form {"data":"VALUE"}'})

    try:
        data = dict(request.json)
        sentence = data["sentence"]

        result = SentimentAnalysis.getResult(sentence)


        return json.dumps({"Status": "SUCCESS", "DATA": str(result), "Reason": ""})
    except Exception as e:
        return json.dumps({"Status": "ERROR", "DATA": None, "Reason": str(e)})



#----------------------------------------------------------------------------------------
def startAPIs():
    try:

        app.run(settings.APIHOST, port=(settings.APIPORT), debug=False, threaded=True)

    except Exception as e:
        print "APIs not started Exception (startAPIs ) at : "+str(settings.APIHOST)+":"+str(settings.APIPORT)+" due to :"+str(e)

if __name__=='__main__':
    startAPIs()


