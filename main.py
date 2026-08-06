from flask import Flask, request, session

app = Flask(__name__)
app.secret_key = "usman"


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        session["name"] = name
        return "The session name is " + session.get("name")

    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <style>
            button {
                width: 70px;
                height: 35px;
            }

            input {
                width: 150px;
                height: 35px;
            }
        </style>
    </head>

    <body>
        <form action="/" method="POST">
            <input type="text" name="name" required>
            <button type="submit">Submit</button>
        </form>
    </body>
    </html>
    '''


app.run(debug=True)