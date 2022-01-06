from flask import Flask, jsonify, request
from keras.models import load_model

# initialize our Flask application
app= Flask(__name__)
@app.route("/name", methods=["POST"])
def setName():
    if request.method=='POST':
        posted_data = request.get_json()
        data = posted_data["array"]
        model = load_model('model.h5')
        classes = model.predict(data)
        if str(classes) == "[[1. 0. 0.]]":
            sendout = "The image you've submitted is classified as a: Paper"
        if str(classes) == "[[0. 1. 0.]]":
            sendout = "The image you've submitted is classified as a: Rock"
        if str(classes) == "[[0. 0. 1.]]":
            sendout = "The image you've submitted is classified as a: Scissors"
        return jsonify(str(str(sendout)))


@app.route("/hello", methods=["GET"])
def hello():
    return "Rock, Paper, and Scissors Image Classification Server.\nTyler Cochran\nDecember 4th, 2021\n"

#  main thread of execution to start the server
if __name__=='__main__':
    app.run(debug=True)
