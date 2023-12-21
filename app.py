from flask import Flask, render_template, jsonify
from twilio.rest import Client
import geocoder

app = Flask(__name__)

account_sid = 'your_twilio_id'

auth_token = 'your_twilio_auth_token'

twilio_phone_number = 'your_twilio_phone_number'

recipient_phone_number = 'recipient_phone_number_mentioned_in_twilio'

def send_location_sms(latitude, longitude):

    client = Client(account_sid, auth_token)

    location_message = f"Latitude: {latitude}, Longitude: {longitude}"

    try:
        message = client.messages.create(
            body=location_message,
            from_=twilio_phone_number,
            to=recipient_phone_number
        )

        return f"Message sent. SID: {message.sid}"

    except Exception as e:
        return f"An error occurred: {str(e)}"

@app.route('/')
def index():
    try:
        location_ip = geocoder.ip('me')
        latitude = location_ip.latlng[0]
        longitude = location_ip.latlng[1]

        location_message = f"Latitude: {latitude}, Longitude: {longitude}"

        return render_template('index.html', location_message=location_message)

    except Exception as e:
        return f"An error occurred: {str(e)}"

@app.route('/send_location')
def send_location():
    try:
        location_ip = geocoder.ip('me')
        latitude = location_ip.latlng[0]
        longitude = location_ip.latlng[1]
        
        result = send_location_sms(latitude, longitude)

        return jsonify({'result': result})

    except Exception as e:
        return jsonify({'result': f"An error occurred: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
