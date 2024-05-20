# Import necessary modules from Flask and related libraries
from flask import Flask, render_template  # Flask for creating the web app, render_template for rendering HTML templates
from flask_wtf import FlaskForm  # FlaskForm for creating forms in Flask
from wtforms import StringField, PasswordField, SubmitField  # Fields for the form: StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length  # Validators for form validation: DataRequired, Email, Length
from flask_bootstrap import Bootstrap5  # Bootstrap5 for styling with Bootstrap

'''
If you see red underlines, it means the required packages are not installed. 
To install the packages, open the Terminal in your IDE (e.g., PyCharm) and run:

On Windows type:
python -m pip install -r requirements.txt

This command will install all the packages listed in the requirements.txt file for this project.
'''

# Define the LoginForm class inheriting from FlaskForm
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])  # Email field with DataRequired validator
    password = PasswordField('Password', validators=[DataRequired()])  # Password field with DataRequired validator
    submit = SubmitField(label="Log In")  # Submit button for the form

# Create an instance of the Flask class
app = Flask(__name__)
# Set a secret key for the session, which is necessary for security purposes
app.secret_key = "any-string-you-want-just-keep-it-secret"
# Initialize Bootstrap5 for this app instance
bootstrap = Bootstrap5(app)

# Define the route for the home page
@app.route("/")
def home():
    return render_template('index.html')  # Render the index.html template for the home page

# Define the route for the login page, allowing both GET and POST methods
@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()  # Create an instance of LoginForm
    # Check if the form is submitted and validated
    if login_form.validate_on_submit():
        # If the email and password match the hardcoded values, render success.html
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            # If the credentials are incorrect, render denied.html
            return render_template("denied.html")
    # If the form is not submitted or not validated, render the login page with the form
    return render_template("login.html", form=login_form)

# If this script is executed directly, run the Flask app in debug mode on port 5001
if __name__ == '__main__':
    app.run(debug=True, port=5001)

