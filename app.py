from flask import Flask
# we're using flask as the lirary

app = Flask(__name__)
# create an instance of the Flask class, which will be our app

@app.route('/')
def home():
    return "Yet is running." 
# when someone visits the page, run the home function,
# and send back the text "Yet is running."

if __name__ == "__main__":
    app.run(debug=True)
    #if this file is run directly, start the server