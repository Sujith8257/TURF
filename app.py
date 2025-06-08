from flask import Flask, render_template, url_for, send_from_directory
import os

app = Flask(__name__, 
    static_url_path='',
    static_folder='static',
    template_folder='templates'
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/my_bookings')
def my_bookings():
    return render_template('my_bookings.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/slot_booking')
def slot_booking():
    return render_template('slot_booking.html')

@app.route('/confirm')
def confirm():
    return render_template('confirm.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

# Serve static files
@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True)
