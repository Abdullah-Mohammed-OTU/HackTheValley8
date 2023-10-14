from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample dataset
BONDS = [
    {"name": "Bond A", "change_in_price": 5},
    {"name": "Bond B", "change_in_price": 10},
    #... add more sample bonds
]

@app.route("/recommend", methods=["POST"])
def recommend_bonds():
    data = request.json

    # Placeholder logic for recommendation (You can replace this with your actual logic)
    recommended_bonds = [bond for bond in BONDS if bond["change_in_price"] < 10] if data["riskType"] == "low" else [bond for bond in BONDS if bond["change_in_price"] >= 10]

    return jsonify(recommended_bonds)

if __name__ == "__main__":
    app.run(debug=True)
