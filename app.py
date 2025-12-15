# app.py
from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

def read_medicines():
    df = pd.read_excel("medicines.xlsx")
    return df.to_dict(orient="records")

@app.route("/", methods=["GET", "POST"])
def home():
    medicines = read_medicines()

    search_result = None
    if request.method == "POST":
        query = request.form.get("search").lower()
        search_result = [m for m in medicines if query in m["Medicine"].lower()]

    return render_template(
        "index.html",
        medicines=medicines,
        search_result=search_result
    )

@app.route("/count")
def count():
    medicines = read_medicines()
    return f"Total medicines: {len(medicines)}"

@app.route("/list")
def list_medicines():
    medicines = read_medicines()
    names = ", ".join([m["Medicine"] for m in medicines])
    return f"Medicines: {names}"

if __name__ == "__main__":
    app.run(debug=True)
