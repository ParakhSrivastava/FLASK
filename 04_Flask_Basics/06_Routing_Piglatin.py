# Set up your imports here!
# import ...
from flask import Flask
app=Flask(__name__)

@app.route('/') # Fill this in!
def index():
    # Welcome Page
    # Create a generic welcome page.
    return '<h1>Welcome!</h1>'

@app.route('/<name>') # Fill this in!
def puppylatin(name):
    # This function will take in the name passed
    # and then use "puppy-latin" to convert it!

    # HINT: Use indexing and concatenation of strings
    # For Example: "hello"+" world" --> "hello world"
    if name[-1]=='y':
        name1= name[:-1]
        name1 = name1 + 'iful'
    elif name[-1]!='y':
        name1= name + 'y'
    
    return '<h1>{}</h1>'.format(name1)

if __name__ == '__main__':
    # Fill me in!
    app.run()
