# Note we imported request- for grabbing info from the site!
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('06-index.html')
  


# This page will have the sign up form
@app.route('/signup_form')
def signup_form():
    return render_template('06-Sign-up.html')



# This page will be the page after the form
@app.route('/thankyou')
def thank_you():
    
    first = request.args.get('first')
    # getting FirstName fro the "form"  
    last = request.args.get('last')
    # getting FirstName fro the "form"  
    
    return render_template('06-thankyou.html',first=first,last=last)


# For displaying when 404 error is found...
@app.errorhandler(404)
def page_not_found(e):
    return render_template('06-404.html'), 404


if __name__ == '__main__':
    app.run()
