from flask import Flask, render_template, request, redirect, url_for, flash
from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Mail config
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your.email@gmail.com'   # sender email
app.config['MAIL_PASSWORD'] = 'your_app_password'

mail = Mail(app)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        user_email = request.form['email']
        user_message = request.form['message']

        # Message to you
        msg_to_owner = Message(
            subject="New Contact Form Message",
            sender=app.config['MAIL_USERNAME'],
            recipients=['debabrata.1331.ind@ieee.org'],
            body=f"From: {user_email}\n\nMessage:\n{user_message}"
        )
        mail.send(msg_to_owner)

        # Auto reply to visitor
        auto_reply = Message(
            subject="Thank you for contacting Debabrata Sahoo!",
            sender=app.config['MAIL_USERNAME'],
            recipients=[user_email],
            body="Thank you for contacting me. I have received your message and will look into the matter soon."
        )
        mail.send(auto_reply)

        flash("Message sent successfully! ✅", "success")
        return redirect('/contact')

    return render_template('contact.html')


app = Flask(__name__)
app.secret_key = 'your-secret-key'  # Needed for flashing messages

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/achievements')
def achievements():
    return render_template('achievements.html')
  
@app.route('/skills')
def skills():
    return render_template('skills.html')  

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        # Basic form validation
        if not all([name, email, subject, message]):
            flash("All fields are required.")
            return redirect(url_for('contact'))

        # Handle submission logic (save to DB, send email, etc.)
        print(f"Contact Form Submitted:\nName: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}")

        flash("Message sent successfully!")
        return redirect(url_for('thank_you'))

    return render_template('contact.html')

@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')

import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

