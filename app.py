from flask import Flask, render_template, request, redirect, url_for, flash

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
def achievements():
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

