from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def form():
    return render_template("form.html")

@app.route("/create", methods=["POST"])
def create_profile():
    firstname = request.form.get('firstname', '')
    lastname = request.form.get('lastname', '')
    sex = request.form.get('sex', 'Male')  
    status = request.form.get('status', '')
    location = request.form.get('location', '')

    profile = {
        "firstname": firstname,
        "lastname": lastname,
        "sex": sex,
        "status": status,
        "location": location,
    }

    return render_template("profile.html", profile=profile)

if __name__ == "__main__":
    app.run(debug=True)



