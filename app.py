from flask import Flask, render_template, request
import json
import requests
app = Flask(__name__)

headers = {'Authorization':'Key e0aea1a6640d4f40b0be23cec3a9d9df'}
api_url = "https://api.clarifai.com/v2/models/aaa03c23b3724a16a56b629203edc62c/outputs"
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/study_image', methods = ['POST'])
def study_image():

    image_url = request.form['url-input']
    # At this point you have the image_url value from the front end
    # Your job now is to send this information to the Clarifai API
    # and read the result, make sure that you read and understand the
    # example we covered in the slides!

    data = {"inputs":[
    {
    "data":{
    "image":{
    "url":image_url
        }
      }
     }
    ]}
    response = requests.post(api_url, headers=headers, data=json.dumps(data))
    parsed_response = json.loads(response.content)
    result = parsed_response['outputs'][0]['data']['concepts']
    return render_template('home.html', results=result)

if __name__ == '__main__':
    app.run(debug=True)
