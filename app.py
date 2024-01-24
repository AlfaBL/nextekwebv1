from flask import Flask, render_template, request

from your_blueprint import your_blueprint

import os
import smtplib
import ssl

app = Flask(__name__)

# Registrujte Blueprint
app.register_blueprint(your_blueprint)

def send_email(name, email, message):
    host = "smtp.gmail.com"
    port = 465

    username = "vidgogic@gmail.com"
    password = "fhsi iwjl zhce nqww"

    receiver = "vidgogic@gmail.com"
    subject = "New Message Form"

    body = f"Name: {name}\nEmail: {email}\nMessage: {message}"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, f"Subject: {subject}\n\n{body}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        name = request.form.get('Name')
        email = request.form.get('email')
        message = request.form.get('message')

        #Ispis  na konzoli
        print(f"Name: {name}\nEmail: {email}\nMessage: {message}")

        #Pozivanje send_email funkcije za slanje mail-a
        send_email(name, email, message)

        #Vraća na index.html nakon slanja mail-a
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))




