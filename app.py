from flask import Flask, render_template, request, redirect, url_for, flash
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail as SendGridMail
import os

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your-secret-key'  # for flash messages

# Get SendGrid API key from environment
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
if not SENDGRID_API_KEY:
    raise ValueError("SENDGRID_API_KEY environment variable not set.")

sg = SendGridAPIClient(SENDGRID_API_KEY)

# Route Definitions
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')
    
@app.route('/internship')
def about():
    return render_template('internship.html')    

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
        user_email = request.form.get('email')
        user_message = request.form.get('message')
        rating = request.form.get('rating')

        if not all([user_email, user_message, rating]):
            flash("All fields are required.")
            return redirect(url_for('contact'))

        try:
            # Send message to portfolio owner
            message_to_owner = SendGridMail(
                from_email='crackerdeba@gmail.com',  # must be a verified sender in SendGrid
                to_emails='debabrata.1331.ind@ieee.org',
                subject='📬 New Contact Form Message via Portfolio',
                plain_text_content=f"From: {user_email}\nRating: {rating}/10\n\nMessage:\n{user_message}"
            )
            sg.send(message_to_owner)

            # Auto reply to visitor
            reply_message = SendGridMail(
                from_email='crackerdeba@gmail.com',  # same verified sender
                to_emails=user_email,
                subject='🤝 Thank you for contacting Debabrata Sahoo!',
                plain_text_content="Thanks for reaching out. I’ve received your message and will respond soon!"
            )
            sg.send(reply_message)

            flash("Message sent successfully!")

        except Exception as e:
            print(f"SendGrid Error: {e}")
            flash("Sorry, something went wrong while sending your message.")

        return redirect(url_for('thank_you'))

    return render_template('contact.html')

@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')

# Run the app
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
