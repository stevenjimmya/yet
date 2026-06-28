from flask import Flask, render_template, request, jsonify
# we're using flask as the lirary
# render_template allows to find an HTML file 
# in the templates folder and send it to the browser
app = Flask(__name__)
# create an instance of the Flask class, which will be our app

@app.route('/')
def home():
    return render_template('index.html') 
# when someone visits the page, run the home function,
# and send back the HTML template.


@app.route('/set_intention', methods=['POST'])
def set_intention():
    data = request.get_json()
    intention = data.get('intention')
    print("Intention set:", intention)
    return jsonify({"status": "success"})


if __name__ == "__main__":
    app.run(debug=True)
    #if this file is run directly, start the server

