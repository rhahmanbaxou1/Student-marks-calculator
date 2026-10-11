from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()

    name = data["name"]
    maths = float(data["maths"])
    accounting = float(data["accounting"])
    computer = float(data["computer"])

    average = (maths + accounting + computer) / 3

    result = "Pass" if average >= 50 else "Fail"

    return jsonify({
        "name": name,
        "average": round(average, 2),
        "result": result
    })


if __name__ == "__main__":
    app.run(debug=True)
